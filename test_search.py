# Gong
import pytest
import yaml

from appnium1.xueqiu.page.app import App


class TestSearch():
    def setup(self):
        self.app = App()

    # 对测试数据进行数据驱动
    @pytest.mark.parametrize("name", yaml.safe_load(open("./test_search.yaml", encoding="utf-8")))
    def test_search(self, name):
        self.app.start()
        self.search = self.app.main().goto_market().goto_search()
        self.search.search(name)
        # 判读是否选择，如果选择先取消
        if self.search.is_choose(name):
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)

if __name__ == '__main__':
    pytest.main()


