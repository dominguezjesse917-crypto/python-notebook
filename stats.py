"""
Compute count, sum, average, min, max from comma-separated numbers.
Run: python list_stats_simple.py
Example input: 10, 7, 3.5, 20
"""
raw = input("Enter numbers separated by commas: ").strip()
# Split by comma, strip spaces, convert to float
nums = [float(x) for x in raw.split(",") if x.strip()]

if not nums:
    print("No numbers provided.")
else:
    total = sum(nums)
    count = len(nums)
    avg = total / count
    print(f"Count: {count}")
    print(f"Sum  : {total}")
    print(f"Avg  : {avg}")
    print(f"Min  : {min(nums)}")
    print(f"Max  : {max(nums)}")
