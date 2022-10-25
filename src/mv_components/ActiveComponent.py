class ActiveComponent:

    @classmethod
    def get_active_items(cls, __active__: str) -> list:
        cls.attributes = __active__.split("|")
        return cls

    @classmethod
    def prepend_hx(cls, attributes: list) -> str:
        cls.output: str = ""
        cls.link = ""
        cls.method = ""
        for attribute in attributes:
            if attribute.split("=")[0] == "method":
                cls.method = attribute.split("=")[1]
            if attribute.split("=")[0] == "link":
                cls.link = attribute.split("=")[1]

            else:
                print(attribute)
                cls.output += f'hx-{attribute.split("=")[0]}=' + attribute.split("=")[1] + " "
                #print(cls.output)
        cls.output += f'hx-{cls.method}=' + cls.link + " "
        return cls

    @classmethod
    def build(cls, __active__):
        cls.get_active_items(__active__)
        cls.prepend_hx(cls.attributes)
        return cls.output
