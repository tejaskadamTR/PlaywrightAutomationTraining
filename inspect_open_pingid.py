"""
Inspect an already-open PingID window
Run this AFTER manually opening PingID.exe
"""

import time
from pingid_automation import PingIDAutomation


def main():
    print("=" * 70)
    print("PingID Window Inspector - Connect to Open Window")
    print("=" * 70)
    print("\nMAKE SURE: PingID.exe is already open before running this!")
    print("=" * 70)

    pingid = PingIDAutomation()

    # Try to connect to existing window
    print("\n[1/2] Looking for open PingID window...")

    if not pingid.connect_to_pingid_window():
        print("\n❌ Could not find PingID window")
        print("\nPlease:")
        print("1. Open PingID.exe manually")
        print("2. Wait for the window to appear")
        print("3. Run this script again")
        return

    print("✅ Connected successfully!")

    # Print detailed window information
    print("\n[2/2] Inspecting controls...")
    print("=" * 70)

    pingid.print_window_info()

    print("\n" + "=" * 70)
    print("✅ Inspection Complete!")
    print("=" * 70)

    print("\nWhat to look for:")
    print("  📝 Edit controls - These are input fields (PIN input)")
    print("  🔘 Button controls - These are buttons (Next, Copy)")
    print("\nNext steps:")
    print("  1. Find the Edit control for PIN input")
    print("  2. Find Button controls for 'Next' and 'Copy'")
    print("  3. Update pingid_automation.py with correct identifiers")


if __name__ == "__main__":
    main()
