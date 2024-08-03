import subprocess
import sys

def assemble_to_prg(asm_file, prg_file):
    try:
        # Run 64tass to assemble the .asm file into a .prg file
        result = subprocess.run(['64tass', '--cbm-prg', asm_file, '-o', prg_file, '-L', 'listing.txt'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        # Check if there were any errors during assembly
        if result.returncode == 0:
            print(f"Successfully assembled {asm_file} to {prg_file}")
        else:
            print(f"Error during assembly: {result.stderr.decode('utf-8')}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Assembly failed: {e.stderr.decode('utf-8')}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python assemble.py <source.asm> <output.prg>")
        sys.exit(1)

    asm_file = sys.argv[1]
    prg_file = sys.argv[2]

    assemble_to_prg(asm_file, prg_file)


