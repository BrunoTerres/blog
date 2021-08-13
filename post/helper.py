class Conversor:

    @staticmethod
    def model_dict(model, campos=[], ignore=[]) -> dict:
        dic = model.__dict__
        dic.__delitem__("_state")

        if campos:
            _dic = {}
            [_dic.update({c: dic[c]}) for c in campos]
            dic = _dic
        elif ignore:
            for i in ignore:
                dic.__delitem__(i)
        return dic

    @staticmethod
    def models_dict(models=[], campos=[], ignore=[]) -> list:
        return [Conversor.model_dict(model, campos=campos, ignore=ignore) for model in models]
