class Scene:
    def __init__(self, x, *args):
        self.list = []
        self.list.append(x)
        for i in args:
            self.list.append(i)

    # need to finish. iterate over all objects in scene. find closest intersection and fill in hit_info.
    # def find_closest_intersection(self, ray,hit_info):
    #     for obj in self.list:
    #         if obj.intersect(ray, hit_info)
    #         f hitDistance > intersect > -1.0:
    #             hitDistance = intersect
    #             hitObject = sphere
