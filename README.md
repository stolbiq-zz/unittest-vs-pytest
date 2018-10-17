# pytest-vs-unittest
Comparison between pytest and unittes test frameworks

##Comparison Table

| Feature                    | Pytest                             | Unittest                         | Winner   |
|----------------------------|------------------------------------|----------------------------------|----------|
| Installation               | Third Party                        | Built in                         |Unittest  |
| Basic Infrastructure       | Can be only a function             | Inheritance                      |Pytest    |
| Basic Assertion            | Builtin assert                     | TestCase instance methods        |Pytest    |
| Flat is better than nested | Function (1 level)                 | Method (2 level)                 |Pytest    |
| Can run each other test    | Can run unittest tests             | Can't pytest test                |Pytest    |
| Test Result on console     | Error Highlight, code snippet      | Only line error, no highlight    |Pytest    |
| Multi param test           | Yes, parameterize, keep flat       | Yes, sub-test, inscrease nesting |Pytest    |
| Test setup                 | Fixture: module, session, function | Template methode: setUp, tearDown|Pytest    |
| Name Refactoring           | Poor, because of name conventions  | Rich, regular object orientaition|Unittest  |
| Running Failed Tests       | Build in --ff, --lf                | Your own way                     |Pytest    |
| Marks                      | Use marks                          | Your own way                     |Pytest    |
