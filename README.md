### Наша идея 🚽
<br />1) Чистим изначальный корпус, чтобы научить потом на нем модель: 
  * удаляем теги, оставляем только текст
  * лемматизируем
  * делаем по предложению на строчке

☀  код - 
[corpus_cleaning+collocations.ipynb](https://github.com/mmtsfasman/NLP_Project/corpus%20cleaning%20%2B%20collocations.ipynb)

☀  результат - 
[corpus.txt](https://drive.google.com/file/d/1M0gFiuZGunLa1v96ZawhI6S9f9Kv604a/view?usp=sharing)

<br /> 2) Преобразуем изначальный корпус в табличку, чтобы потом искать позитивные и негативные оценки в нем. Gервая колонка - текст, остальные 3 колонки - оценки (food/service/interior). 

| Text | Food | Service | Interior |
| --- |:---:| ---:|-----:|
| ...|...| ...|...|

☀ код - 
[to_csv.py](https://github.com/mmtsfasman/NLP_Project/to_csv.py)
☀ конечный файл - 
[corpus.csv](https://github.com/mmtsfasman/NLP_Projectr/corpus.csv)
<br />
<br />
3) Обучаем word2vec на корпусе из п. 1 (corpus.txt)
<br /> ☀ код - 
[word2vec&most_similar.ipynb](https://github.com/mmtsfasman/NLP_Project/word2vec%20%26%20most_similar%20lists.ipynb)

☀ результат - 
[my.model](https://github.com/mmtsfasman/NLP_Project/my.model)
<br />
<br />
4) Составляем список слов, близких к словам из seed (исключая коллокации), через функцию most_similar
> Исходим из того, что таким образом можно расширить список оценочных слов.

 ☀ код - [word2vec&most_similar.ipynb](https://github.com/mmtsfasman/NLP_Project/word2vec%20%26%20most_similar%20lists.ipynb)

 ☀ результат - там же
<br />
<br />
5) Используем ту же функцию и ту же модель, чтобы составить список слов близких к еде, сервису, интерьеру
Формат
<br /> ☀ Код - 
[word2vec&most_similar.ipynb](https://github.com/mmtsfasman/NLP_Project/word2vec%20%26%20most_similar%20lists.ipynb)

 ☀ Результат - там же
<br />
<br />
6) Чистим руками списки из п. 4 и п. 5
<br />
(6.1) Список слов по категориям  -  ☀ [здесь](https://github.com/mmtsfasman/NLP_Project/word2vec%20%26%20most_similar%20lists.ipynb)
лежит код, который выдавал мне каждое слово, а я писала 1 если оно подходит, ничего - если его не надо исключить из списка.  ☀ Конечный вид - json со словарем вида {'food':[word1, ...,wordn], 'service':[word1, ...,wordn], 'interior':[word1, ...,wordn]} ☀ Результат -
[param.json](param.json)

<br />
(6.2) Расширенный список seed ☀ результат - 
[seed_extended.txt](seed_extended.txt)  

<br />7) Составляем список самых частотных и специфичных триграмм - как оказалось, этого достаточно, чтоб получить список оценочных коллокаций
<br />
<br />
8) Берем список слов близких к еде, сервису, интерьеру из п.5, проходим по нему, выбираем предложения, содержащие эти слова, смотрим на их оценку по соответствующему параметру (food/service/interior). Смотрим, какие из оценочных слов из п. 4 в них используются, по оценке определяем их тональнальность pos/neg/ambi.
<br />
<br />

**Роли:** <br />
🚀 п. 1 - Соня Стырина <br />
🚀 п. 2 - Саша Пивоваров <br />
🚀 п. 3 - Маша Цфасман <br />
🚀 п. 4 - Света Клименко <br />
🚀 п. 5 - Маша Цфасман <br />
🚀 п. 6.1 - Маша Цфасман <br />
🚀 п. 6.2 - Света Клименко <br />
🚀 п. 7 - Соня Стырина <br />
🚀 п. 8 - Саша Пивоваров <br />




