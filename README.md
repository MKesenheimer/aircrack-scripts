# aircrack-scripts
Helper scripts for aircrack-ng

## Usage
Remove pcap files from a folder that do not contain any handshakes:
```
python3 remove-zero-handshakes.py /path/to/pcap/folder
```

Convert all pcap files to hccapx and combine them into one single `combined.hccapx` file:
```
./convert-combine-handshakes.sh /path/to/pcap/folder
```
