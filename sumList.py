def sumList(list):
  sum = 0

  if len(list) == 1:
    return list[0]
  else:
    sliceList = list[1::]
    sumList(sliceList)
    sum += list[0]

  if __name__ == "__main__":
    list = [0, 1, 4, 7]
    sumList(list)
