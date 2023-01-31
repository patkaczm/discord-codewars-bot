from data.cw_task import CwTask


class TestCwTask:
    kyu = 6
    name = "some name"
    cw_id = "0xdeadbeef"

    def test_cw_task_created_without_id_has_id_fixed(self):
        t = CwTask(kyu=self.kyu, name=self.name, cw_id=self.cw_id)
        assert t.kyu == self.kyu
        assert t.name == self.name
        assert t.cw_id == self.cw_id
        assert t.id == -1

    def test_cw_task_created_with_id_has_id(self):
        id = 13
        t = CwTask(id=id, kyu=self.kyu, name=self.name, cw_id=self.cw_id)
        assert t.id == id
