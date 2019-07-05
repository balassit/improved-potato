class ExtendibleArray:
    def __init__(self):
        self.old = None
        self.new = [None]
        self.shadow = -1
        self.end = 1

    def getlist(self):
        return list(filter(None.__ne__, self.new + self.old))

    def getItems(self):
        return str(list(filter(None.__ne__, self.new + self.old))).strip("[]")

    def add(self, item):
        if self.end == len(self.new):
            self.old = self.new
            self.new = [None] * 2 * len(self.new)
            self.shadow = self.end - 1
        self.new[self.end] = item
        self.new[self.shadow] = self.old[self.shadow]
        self.old[self.shadow] = None
        self.end = self.end + 1
        self.shadow = self.shadow - 1
        return True

    def get(self, index):
        if index < 0 and index >= self.size():
            print(f"Index {index}, size {self.size()}")
        if index + 1 <= self.shadow:
            return self.old[index + 1]
        else:
            return self.new[index + 1]

    def size(self):
        return self.end - 1

    def set(self, index, value):
        original = self.get(index)
        if index + 1 <= self.shadow:
            self.old[index + 1] = value
        else:
            self.new[index + 1] = value
        return original

    def remove(self, index):
        # Grab the value of the element we're removing; this also verifies the index.
        result = self.get(index)
        # 1 > -1
        if index + 1 > self.shadow:
            # shfit elements past this element down on top of the element
            self.new[index + 1 :] = self.new[index + 2 :]
            # Move the element before the shadow down.
            self.old[self.shadow + 1] = self.new[self.shadow + 1]
            # To be nice to the garbage collector, clear the endpoints.
            self.new[self.shadow + 1] = None

            # Pull the shadow and endpoint closer together.
            self.shadow = self.shadow + 1
            self.end = self.end - 1
        else:
            self.old[index + 1 :] = self.old[index + 2 :]
            for i in range(2):
                self.old[self.shadow + 1 + i] = self.new[self.shadow + 1 + i]
            self.shadow = self.shadow + 1

            #     # Shuffle the elements of the new array down one position.
            #     # The beginning position is one past the shadow, as it always is.
            self.old[index + 1 :] = self.old[index + 2 :]

            # Clear the element that just got moved. */
            self.new[self.end - 1] = None

            # Back up the end position, since we just lost an element. */
            self.end = self.end - 1

        # Finally, see if we just emptied the new array.  This happens if
        # the end pointer is one step past the shadow pointer.
        if self.end == self.shadow + 1:
            # Drop the new array and promote the old array to new.
            self.new = self.old
            # Make a blank array for new elements.
            self.old = [None] * (int(len(self.new) / 2))
            # Move the end and shadow pointers off the ends of the array.
            self.shadow = -1
            self.end = len(self.new)

        return result
