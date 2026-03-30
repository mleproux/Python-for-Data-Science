class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result: float = 0
        for i in range(len(V1)):
            result = result + (V1[i] * V2[i])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        V3: list[float] = []
        for i in range(len(V1)):
            V3.append(float(V1[i]) + float(V2[i]))
        print(f"Add product is : {V3}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        V3: list[float] = []
        for i in range(len(V1)):
            V3.append(float(V1[i]) - float(V2[i]))
        print(f"Sous product is: {V3}")
