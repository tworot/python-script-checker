import time
import subprocess

def test_script(test_command_list, test_data):
    start_time = time.time()
    test_module = subprocess.Popen(test_command_list, stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE)

    try:
        stdout, stderr = test_module.communicate(test_data[0].encode(), timeout=int(test_data[2]))
        result = str(stdout.decode().strip())
        if result == test_data[1]:
            test_result = (1, 0, 0)
        else:
            test_result = (0, 1, 0)
    except subprocess.TimeoutExpired:
        test_result = (0, 0, 1)
    finally:
        test_module.kill()

    end_time = time.time()
    seconds = end_time - start_time
    return (seconds, *test_result)