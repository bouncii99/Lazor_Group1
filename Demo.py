import Lazor

if __name__ == '__main__':
    g, rflb, ob, rfrb, l, p = Lazor.main()
    # Add block
    Lazor.Board.place_block(g, rflb[0], position=(0, 0))
    print(g)
