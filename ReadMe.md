## Descrição do Código

Este projeto utiliza o `scikit-learn`, uma biblioteca de aprendizado de máquina em Python, para criar um classificador que diferencia entre maçãs e laranjas com base em características de peso e textura. O objetivo é demonstrar como treinar um modelo de árvore de decisão para a classificação de frutas.

## Explicação do Código

1. **Importação da Biblioteca**:

    ```python
    from sklearn import tree
    ```

    Importa o módulo de árvore de decisão do `scikit-learn`, que será utilizado para criar o classificador.

2. **Definição de Variáveis**:

    ```python
    liso = 1
    irregular = 0
    maca = 5
    laranja = 10
    ```

    Define valores numéricos para texturas (`liso` e `irregular`) e tipos de frutas (`maca` e `laranja`).

3. **Conjunto de Dados de Treinamento**:

    ```python
    X = [[140, liso], [130, liso], [150, irregular], [170, irregular]]
    Y = [maca, maca, laranja, laranja]
    ```

    - `X`: Lista de características das frutas, onde o primeiro valor é o peso e o segundo é a textura (liso ou irregular).
    - `Y`: Lista de rótulos correspondentes, indicando se a fruta é uma maçã ou uma laranja.

4. **Treinamento do Modelo**:

    ```python
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    ```

    - Cria um classificador de árvore de decisão (`DecisionTreeClassifier`) e o treina usando os dados de entrada `X` e os rótulos `Y`.

5. **Predição e Classificação**:

    ```python
    print("maca" if clf.predict([[100, 1]]) == maca else "laranja")
    ```

    - O modelo faz uma predição com base em uma nova entrada `[100, 1]` (fruta de 100g com textura lisa).
    - O código imprime `"maca"` se o modelo identificar a entrada como uma maçã, ou `"laranja"` caso contrário.

## Observações

- O código é um exemplo básico de como usar árvores de decisão para tarefas de classificação simples.
- O modelo é treinado com um pequeno conjunto de dados de frutas, e as predições são baseadas no aprendizado adquirido.
