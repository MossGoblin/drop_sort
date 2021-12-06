def sort(bucket):
    result = []
    for item in bucket:
        placed = False
        if len(result) == 0:
            result.append(item)
            continue
        for placed_item in result:
            if item <= placed_item:
                result.insert(result.index(placed_item), item)
                placed = True
                break
        if not placed:
            result.append(item)
    
    return result