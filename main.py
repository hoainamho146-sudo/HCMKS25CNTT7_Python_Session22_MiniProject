"""
Smart Energy Monitor
"""

import logging

from energy_logic import (
    show_devices,
    update_indices,
    activate_overload,
    calculate_energy_financials
)


def display_menu():
    """
    Display main menu.
    """
    print("\n========== SMART ENERGY ==========")
    print("1. Xem danh sách thiết bị")
    print("2. Cập nhật chỉ số điện")
    print("3. Kích hoạt cảnh báo")
    print("4. Tính chi phí năng lượng")
    print("5. Thoát")
    print("==================================")


def main():
    """
    Main controller.
    """
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )

    devices = [
        {
            "id": "M01",
            "location":
                "Mechanical Shop A",
            "old_index": 1200,
            "new_index": 4500,
            "status": "Normal"
        },
        {
            "id": "M02",
            "location":
                "Assembly Line B",
            "old_index": 2300,
            "new_index": 8500,
            "status": "Overload"
        },
        {
            "id": "M03",
            "location":
                "Packaging Area",
            "old_index": 5000,
            "new_index": 20000,
            "status": "Normal"
        }
    ]

    while True:
        display_menu()

        try:
            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

        except ValueError:
            print(
                "Vui lòng nhập số từ 1-5."
            )
            continue

        if choice == 1:
            show_devices(devices)

        elif choice == 2:
            update_indices(devices)

        elif choice == 3:
            activate_overload(devices)

        elif choice == 4:
            (
                total_kwh,
                discount,
                final_cost
            ) = calculate_energy_financials(
                devices
            )

            print(
                "\n===== BÁO CÁO NĂNG LƯỢNG ====="
            )

            print(
                f"Tổng điện tiêu thụ: "
                f"{total_kwh:,.0f} kWh"
            )

            print(
                f"Chiết khấu áp dụng: "
                f"{discount}%"
            )

            print(
                f"Tổng chi phí: "
                f"{final_cost:,.0f} VND"
            )

        elif choice == 5:
            print(
                "\nCảm ơn bạn đã sử dụng "
                "Smart Energy Monitor!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ."
            )


if __name__ == "__main__":
    main()
