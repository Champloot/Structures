class Tree:
    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    # Проверка наличия у узла значения
    def isempty(self):
        return self.value == None

    # Проверка отсутствия дочерних элементов
    def isleaf(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False

    # Вставка нового элемента
    def insert(self, data):
        # Если узел пустой, вставляем сюда
        if self.isempty():
            self.value = data
            # Создаем также пустые левый и правый узлы
            self.left = Tree()
            self.right = Tree()
            print(f"{self.value} is inserted.")

        # Если элемент <, идем в левый дочерний узел
        elif data < self.value:
            self.left.insert(data)
            return
        # Если элемент >=, то в правый
        elif data >= self.value:
            self.right.insert(data)
            return
        return "Error"

    def getMax(self):
        if self.right.right == None:
            return self.value
        else:
            return self.right.getMax()

    def getMin(self):
        if self.left == None:
            return self.value
        else:
            return self.left.getMin()

    # Поиск элемента
    def search(self, data):
        # Если в том месте, где элемент мог бы быть
        # этого элемента нет, то его нет в дереве
        if self.isempty():
            print(f"{data} is not found")
            return False
        # Если нашли
        if self.value == data:
            print(f"{data} is found")
            return True
        # Если значение элемента < значения в данном узле
        if data < self.value:
            return self.left.search(data)
        # Если >=
        elif data >= self.value:
            return self.right.search(data)
        return "Error"

    def delete(self, data):
        if self.isempty():
            return
        elif data < self.value:
            self.left.delete(data)
            return
        elif data > self.value:
            self.right.delete(data)
            return
        elif data == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
            elif self.right.isempty():
                self.value = self.left.value
                self.left = self.left.left
                self.right = self.left.right
            else:
                self.value = self.left.getMax()
                self.left.delete(self.value)
                return

    # Симметричный обход
    # для проверки верности установившегося порядка узлов
    def show_inorder(self):
        if self.value == None:
            return []
        else:
            return self.left.show_inorder() + [self.value] + self.right.show_inorder()

    # Обратный обход
    # позволяет безопасно удалить все узлы дерева
    # в языках с ручным управления памятью
    # при таком обходе всегда сначала удаляется узел "лист"
    # так в памяти никто забыт не будет
    def show_preorder(self):
        if self.value == None:
            return []
        else:
            return self.left.show_preorder() + self.right.show_preorder() + [self.value]

    # Прямой обход
    # используется при копировании дерева в памяти
    # так мы идем по узлам в том порядке
    # в каком они были размещены в дереве сверху вниз
    def show_postorder(self):
        if self.value == None:
            return []
        else:
            return [self.value] + self.left.show_postorder() + self.right.show_postorder()


# Пример
T = Tree(5)
T.insert(1)
T.insert(8)
T.insert(3)
T.insert(9)
T.insert(2)
T.insert(6)
T.insert(7)
print("Дерево до удаления: ", T.show_inorder())
T.delete(6)
print("Дерево после удаления: ", T.show_inorder())
print("Обратный обход", T.show_preorder())
print("Прямой обход", T.show_postorder())
