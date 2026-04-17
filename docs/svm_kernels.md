# Kernels en SVM

## ¿Qué es una SVM?

Las SVM (Support Vector Machine) son modelos que se usan para clasificar datos. Básicamente, lo que hacen es tratar de separar los datos en grupos usando una línea (si estamos en 2D) o un plano (en más dimensiones).

---

## El problema

El tema es que no siempre se puede separar todo con una línea recta.

Por ejemplo, si los datos están distribuidos en forma de círculo o mezclados de manera rara, una línea no alcanza para separarlos bien.

---

## Entonces, ¿qué hace un kernel?

El kernel es una forma de “acomodar” los datos para que se puedan separar.

En lugar de intentar separarlos como están, lo que hace es llevarlos a otro espacio (otra dimensión) donde sí se puedan dividir con una línea o un plano.

---

## ¿Cómo funciona en la práctica?

* Primero tenés los datos originales, que están mezclados
* Después el kernel los transforma
* Y en ese nuevo espacio, ahora sí se pueden separar

Lo importante es que esta transformación no se hace de forma explícita, sino que el modelo la aplica directamente.

---

## Tipos de kernels

### Lineal

Es el más simple. Sirve cuando los datos ya se pueden separar más o menos bien con una línea.


![Kernel lineal](https://www.researchgate.net/profile/Elisa-Aleman-Carreon/publication/323137738/figure/fig2/AS:735529951842304@1552375414012/D-example-of-the-Linear-SVM-classification-The-linear-kernel-for-the-SVM-classification.png)

Este kernel se utiliza cuando los datos pueden separarse mediante una línea recta. 
El modelo busca el hiperplano que maximiza la distancia entre las clases.

### Polinómico

Permite hacer separaciones más curvas. Es útil cuando los datos tienen cierta complejidad.


![Kernel polinómico](https://media.geeksforgeeks.org/wp-content/uploads/20250121155050429170/non_linear_svm_polynomial_kernel.png)

El kernel polinómico permite separar datos cuando no se pueden dividir con una línea recta. En lugar de una frontera lineal, genera curvas que se adaptan mejor a la forma de los datos. Es útil cuando la relación entre variables es no lineal, pero no demasiado compleja.

### RBF (Radial)

Es el más usado. Se adapta bastante bien a datos complejos y permite separar casos donde otras opciones no funcionan.


![Kernel RBF](https://miro.medium.com/v2/resize:fit:1400/1*kO_kAQ32-qmT-iljdZdkrQ.png)

El kernel RBF permite separar datos complejos utilizando la distancia entre los puntos. Genera fronteras suaves y no lineales, adaptándose a la forma de los datos. Es uno de los kernels más utilizados porque puede manejar patrones muy complejos de manera eficiente.

---

## Conclusión

Los kernels hacen que las SVM sean mucho más flexibles. Gracias a esto, el modelo puede manejar situaciones donde los datos no son fáciles de separar, sin necesidad de cambiar completamente el enfoque.
