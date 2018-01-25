def main():
  x = 50
  y = x << 1

  print("{}\t\t{}\t\t{}".format(x, bin(x), hex(x)))
  print("{}\t\t{}\t\t{}".format(y, bin(y), hex(y)))

if __name__ == '__main__':
    main()
