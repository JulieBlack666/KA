from collections import deque


class CycleChecker:
    def __init__(self, input_file='in.txt', output_file='out.txt'):
        self.output_file = output_file
        self.nodes_count = 0
        self.matrix = []
        self.init_graph(input_file)

    def init_graph(self, in_file):
        with open(in_file) as file:
            self.nodes_count = int(file.readline())
            for line in file:
                self.matrix.append([int(i) for i in line.split()])

    def find_cycle(self):
        track = {0: -1}
        has_cycle = False
        queue = deque()
        queue.append(0)
        end_nodes = ()
        while queue:
            node = queue.popleft()
            for i in range(node, self.nodes_count):
                if self.matrix[node][i] == 1:
                    if i in track.keys():
                        has_cycle = True
                        end_nodes = deque([i, node])
                        break
                    queue.append(i)
                    track[i] = node
            if has_cycle:
                break
        self.write_result(has_cycle, self.collect_nodes_in_cycle(end_nodes, track))

    @staticmethod
    def collect_nodes_in_cycle(end_nodes, track):
        result = []
        while end_nodes:
            current = end_nodes.popleft()
            next = track[current]
            if current in result:
                break
            end_nodes.append(next)
            result.append(current)
        return sorted(result)

    def write_result(self, has_cycle, result_nodes):
        with open(self.output_file, 'w') as file:
            if has_cycle:
                file.write("N\n")
                for node in result_nodes:
                    file.write(str(node) + ' ')
            else:
                file.write("A")


if __name__ == '__main__':
    checker = CycleChecker()
    checker.find_cycle()
