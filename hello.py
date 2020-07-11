from PIL import Image

def init(block, image):
    img = Image.open(image)
    width, height = img.size
    color = img.load()
    print(img.format, img.size, img.mode)
    print(width/block, height/block, (width/block)*(height/block))

    # 为了处理最后的区块，加了一次循环
    max_width = width + block
    max_height = height + block
    for x in range(block - 1, max_width, block):
        for y in range(block - 1, max_height, block):
            # 如果是最后一次循环，则x坐标等于width - 1
            if x == max_width - max_width % block - 1:
                x = width - 1
            # 如果是最后一次循环，则x坐标等于height - 1
            if y == max_height - max_height % block - 1:
                y = height - 1
            # 改变每个区块的颜色值
            merge_block(x, y, block, color)
            y+=block
        x+=block

    img.save("pixel.png")
    img.show()

def merge_block(x, y, block, color):
    color_dist = {}
    block_pos_list = []
    for pos_x in range(-block + 1, 1):
        for pos_y in range(-block + 1, 1):
            # todo print(x + pos_x,y + pos_y)
            block_pos_list.append([x + pos_x, y + pos_y])
    for pixel in block_pos_list:
        if not str(color[pixel[0], pixel[1]]) in color_dist.keys():
            color_dist[str(color[pixel[0], pixel[1]])] = 1
        else:
            color_dist[str(color[pixel[0], pixel[1]])] += 1
    # key-->value => value-->key
    new_dict = {v: k for k, v in color_dist.items()}
    max_color = new_dict[max(color_dist.values())]
    # 将区块内所有的颜色值设置为颜色最多的颜色
    for a in block_pos_list:
        color[a[0], a[1]] = tuple(list(map(int, max_color[1:len(max_color) - 1].split(","))))


if __name__ == "__main__":
    init(4, "24.jpg")