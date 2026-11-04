import statistics
import subprocess
import time

PAT = "./pat"
SOURCE = "test/examples/savina/ping_pong.pat"
SIZES = [5, 1000, 10000, 100000]
RUNS = 5  # timed runs per measurement after one discarded warm-up run


#TODO: change that fr the regex and command line arguments stuff and delte the 1 time time deleteion thingy
#eval.ml, common/lib_types, bin/main.ml store into settings.ml
'''

#TODO: WORKKKKKKKKKKKKKKKKKKKKKK!!!!!
no-io check no-io and dont print if set

command line, no-print, tiem interprerter onlyy


'''

def median_ms(args):
    times = []
    for _ in range(RUNS + 1):
        start = time.perf_counter()
        subprocess.run(args, check=True, stdout=subprocess.DEVNULL)
        times.append((time.perf_counter() - start) * 1000)
    return statistics.median(times[1:])


def main():
    print(f"{'pings':>8} {'total ms':>10} {'typecheck ms':>13} {'runtime ms':>11}")
    for n in SIZES:
        program_args = ["--", "--pings", str(n)]
        total = median_ms([PAT, SOURCE] + program_args)
        typecheck = median_ms([PAT, "-t", SOURCE] + program_args)
        print(f"{n:>8} {total:>10.1f} {typecheck:>13.1f} {total - typecheck:>11.1f}")


if __name__ == "__main__":
    main()
