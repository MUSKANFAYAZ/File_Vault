import time
import os
from Crypto.Random import get_random_bytes
# We need access to the core encryption logic to test it
from . import core

def run_benchmark(file_size_mb, algorithm):
    """
    Measures encryption performance for a given file size and algorithm.
    """
    print(f"\n--- Running Benchmark ---")
    print(f"Algorithm: {algorithm}")
    print(f"Data Size: {file_size_mb} MB")

    # 1. Create a temporary file with random data for the test
    file_size_bytes = file_size_mb * 1024 * 1024
    random_data = get_random_bytes(file_size_bytes)
    temp_file_path = "benchmark_temp_file.bin"
    with open(temp_file_path, "wb") as f:
        f.write(random_data)

    # Use a dummy password, as the strength doesn't affect speed
    password = "benchmark_password"

    # 2. Time the core encryption function
    start_time = time.perf_counter()

    # We call the same function you use for real encryption
    core.encrypt_file_with_password(
        file_path=temp_file_path,
        original_filename="benchmark.bin",
        password=password,
        algorithm=algorithm
    )

    end_time = time.perf_counter()

    # 3. Clean up the temporary file
    os.remove(temp_file_path)

    # 4. Calculate and print the results
    duration = end_time - start_time
    # Throughput is a measure of speed, calculated as Megabytes per second
    throughput = file_size_mb / duration

    print(f"  -> Time taken: {duration:.4f} seconds")
    print(f"  -> Throughput: {throughput:.2f} MB/s")

    return duration, throughput