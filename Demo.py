import Lazor

if __name__ == '__main__':
    g, rflb, ob, rfrb, l, p = Lazor.main()
    # Test position check
    print(Lazor.Board.pos_check(g, 3, 3))
    # Add block
    Lazor.Board.place_block(g, rflb[0], pos=(0, 0))
    print(g)
