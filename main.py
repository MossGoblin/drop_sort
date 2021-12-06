from drop_sort import drop_sort as ds

def main():
    print('== SinkSort ==')
    bucket = [2, 1, 4, 5, 8, 7, 5, 6, 3, 1, 4, 8, 9, 6, 3, 2, 1]
    sorted = ds.sort(bucket)
    print(sorted)
    pass

if __name__ == '__main__':
    main()