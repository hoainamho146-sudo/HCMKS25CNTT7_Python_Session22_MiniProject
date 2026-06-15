"""
Smart Energy Monitor Business Logic
"""

import logging

BASE_RATE = 3000
DISCOUNT_THRESHOLD = 50000
DISCOUNT_RATE = 0.03


def show_devices(devices):
    """
    Display all devices in table format.

    Args:
        devices (list): Device list.
    """
    if not devices:
        print("Hệ thống hiện chưa có thiết bị nào.")
        return

    print("\n===== DANH SÁCH THIẾT BỊ =====")

    print(
        f"{'ID':<6}"
        f"{'LOCATION':<25}"
        f"{'OLD':<10}"
        f"{'NEW':<10}"
        f"{'STATUS':<12}"
    )

    print("-" * 65)

    for device in devices:
        print(
            f"{device['id']:<6}"
            f"{device['location']:<25}"
            f"{device['old_index']:<10}"
            f"{device['new_index']:<10}"
            f"{device['status']:<12}"
        )


def find_device(devices, device_id):
    """
    Find device by id.

    Args:
        devices (list): Device list.
        device_id (str): Device id.

    Returns:
        dict | None
    """
    for device in devices:
        if device["id"].upper() == device_id.upper():
            return device

    return None


def update_indices(devices):
    """
    Update device indices.
    """
    device_id = input(
        "Nhập mã thiết bị: "
    ).strip().upper()

    device = find_device(
        devices,
        device_id
    )

    if device is None:
        print("ERR-E01: Không tìm thấy thiết bị.")
        return

    while True:
        try:
            old_index = float(
                input("Nhập chỉ số cũ: ")
            )

            if old_index < 0:
                print(
                    "Chỉ số phải >= 0."
                )
                continue

            break

        except ValueError:
            print(
                "Vui lòng nhập số hợp lệ."
            )

    while True:
        try:
            new_index = float(
                input("Nhập chỉ số mới: ")
            )

            if new_index < 0:
                print(
                    "Chỉ số phải >= 0."
                )
                continue

            if new_index < old_index:
                print(
                    "ERR-E02: Chỉ số mới "
                    "không được nhỏ hơn "
                    "chỉ số cũ."
                )
                continue

            break

        except ValueError:
            print(
                "Vui lòng nhập số hợp lệ."
            )

    device["old_index"] = old_index
    device["new_index"] = new_index

    logging.info(
        "Device %s updated successfully",
        device_id
    )

    print(
        "Cập nhật chỉ số thành công."
    )


def activate_overload(devices):
    """
    Activate overload warning.
    """
    device_id = input(
        "Nhập mã thiết bị: "
    ).strip().upper()

    device = find_device(
        devices,
        device_id
    )

    if device is None:
        print("ERR-E01: Không tìm thấy thiết bị.")
        return

    if device["status"] == "Overload":
        print(
            "ERR-E04: Thiết bị đã ở "
            "trạng thái Overload."
        )
        return

    consumption = (
        device["new_index"]
        - device["old_index"]
    )

    if consumption > 5000:
        device["status"] = "Overload"

        logging.warning(
            "Overload activated for %s "
            "(Consumption: %.2f kWh)",
            device_id,
            consumption
        )

        print(
            "Đã kích hoạt cảnh báo "
            "quá tải."
        )

    else:
        print(
            "Thiết bị chưa vượt "
            "ngưỡng quá tải."
        )


def calculate_energy_financials(devices):
    """
    Calculate energy financial report.

    Args:
        devices (list)

    Returns:
        tuple:
        (
            total_consumption,
            discount_percent,
            final_cost
        )
    """
    total_consumption = 0

    for device in devices:
        total_consumption += (
            device["new_index"]
            - device["old_index"]
        )

    total_cost = (
        total_consumption
        * BASE_RATE
    )

    discount_percent = 0

    if total_consumption >= (
        DISCOUNT_THRESHOLD
    ):
        discount_percent = 3

        total_cost *= (
            1 - DISCOUNT_RATE
        )

    return (
        total_consumption,
        discount_percent,
        int(total_cost)
    )
