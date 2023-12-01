import sys
import BlendLink as bl

APP_RUNNING = True

ARGUMENTS = sys.argv
PARSED_ARGS = []
THIS_NODE = bl.BLNode()

for i, argument in enumerate(ARGUMENTS):
    if argument.startswith('-') and i > 0:
        PARSED_ARGS.append(argument.removeprefix('-').lower())
    elif i > 0:
        print("Invalid Argument:", i, ":", argument)

# Convert everything in arg list to 'str' type
PARSED_ARGS = [str(arg) for arg in PARSED_ARGS]

for arg in PARSED_ARGS:
    match arg[0:4]:        
        case "main":
            print("Argument Set for Main Server")

        case "remo":
            print("Argument Set Remote Server")

        case "addr":
            print("Argument Server Address:", arg.removeprefix("addr"))

        case "port":
            print("Argument Server Port:", int(arg.removeprefix("port")))


THIS_NODE.SetupNode()


# Main App Loop
while True:
    if not APP_RUNNING:
        break

# Shutdown Procedures Here