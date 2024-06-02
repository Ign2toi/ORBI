import requests
import argparse

def send_requests(url, num_packets):
    try:
        for _ in range(num_packets):
            response = requests.get(url)
            print(f"Sent packet, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    print("████████████████████████████")
    print("█░░░░░░░░░░░░░░░░░░░░░░░░█")
    print("█░░░░░░░░░░░ORBI░░░░░░░░░█")
    print("█░░░░░░░░░░░░░░░░░░░░░░░░█")
    print("████████████████████████████")
    parser = argparse.ArgumentParser(description="Simple tool for sending multiple packets to a target URL")
    parser.add_argument("url", help="Target URL")
    args = parser.parse_args()

    print(f"url: {args.url}")

    num_packets = int(input("Enter the number of packets to send: "))
    num_retries = int(input("Enter the number of retries: "))

    for _ in range(num_retries):
        print(f"Sending {num_packets} packets to {args.url}")
        send_requests(args.url, num_packets)

if __name__ == "__main__":
    main()
