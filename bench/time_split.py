import statistics
import subprocess

PAT = "./pat"
SOURCE = "test/examples/savina/ping_pong.pat"
SIZES = [5, 1000, 10000, 100000]
RUNS = 5


def interpreter_ms(pings):
    result = subprocess.run(
        [PAT, "--no-print", "--time-interpreter", SOURCE, "--", "--pings", str(pings)],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stderr)


def main():
    print(f"{'pings':>8} {'interpreter ms':>15}")
    for n in SIZES:
        times = [interpreter_ms(n) for _ in range(RUNS)]
        print(f"{n:>8} {statistics.median(times):>15.1f}")


if __name__ == "__main__":
    main()
