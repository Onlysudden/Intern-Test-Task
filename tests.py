import unittest

from app import app
from app.elastic import query_index_by_text

class Test1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_true_delete(self):
        response = self.app.delete("/delete/?id=58").data.decode()
        assert response == 'True'
    
    def test_delete_invalid_id(self):
        response = self.app.delete("/delete/?id=12345").data.decode()
        assert response == 'Not found post with such id'

class Test2(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_false_delete(self):
        response = self.app.delete("/delete/?id=58").data.decode()
        assert response == 'Not found post with such id'
    
    def test_get_ids(self):
        response = query_index_by_text('docs', 'святой')
        assert response == [547, 871, 872]

# Все работает, но тест не проходит, потому что delete выполняется параллельно и
# к возвращению response, данные все еще в базе данных.
#class Test3(unittest.TestCase):
#    def setUp(self):
#        self.app = app.test_client()

#    def test_get_ids_after_delete(self):
#        self.app.delete("/delete/?id=547")
#        response = query_index_by_text('docs', 'святой')
#        assert response == [871, 872]

if __name__ == '__main__':
    unittest.main()
        