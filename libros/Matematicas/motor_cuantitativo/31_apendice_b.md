# Apéndice B: Cheat Sheets de Fórmulas Matemáticas

## Álgebra Lineal

### Vectores

| Operación | Fórmula | Python |
|-----------|---------|--------|
| Norma L2 | \|\|v\|\| = √(Σ vᵢ²) | `np.linalg.norm(v)` |
| Producto punto | v·w = Σ vᵢwᵢ | `v @ w` o `np.dot(v, w)` |
| Ángulo | cos(θ) = (v·w) / (\|\|v\|\|·\|\|w\|\|) | `np.arccos(dot/(n1*n2))` |

### Matrices

| Operación | Fórmula | Python |
|-----------|---------|--------|
| Transpuesta | (A^T)ᵢⱼ = Aⱼᵢ | `A.T` |
| Multiplicación | (AB)ᵢⱼ = Σₖ Aᵢₖ Bₖⱼ | `A @ B` |
| Inversa | A·A⁻¹ = I | `np.linalg.inv(A)` |
| Determinante | det(A) | `np.linalg.det(A)` |
| Eigenvalores | Av = λv | `np.linalg.eig(A)` |
| SVD | A = UΣV^T | `np.linalg.svd(A)` |

### Ecuación Normal (Regresión Lineal)

```
β = (X^T X)^(-1) X^T y
```

```python
beta = np.linalg.inv(X.T @ X) @ X.T @ y
```

## Estadística Descriptiva

| Métrica | Fórmula | Python |
|---------|---------|--------|
| Media | x̄ = (1/n) Σ xᵢ | `np.mean(x)` |
| Mediana | Valor central ordenado | `np.median(x)` |
| Varianza (pob) | σ² = (1/n) Σ(xᵢ - μ)² | `np.var(x)` |
| Varianza (mue) | s² = (1/(n-1)) Σ(xᵢ - x̄)² | `np.var(x, ddof=1)` |
| Desv. estándar | s = √s² | `np.std(x, ddof=1)` |
| Asimetría | γ₁ = (1/n) Σ((xᵢ - x̄)/s)³ | `scipy.stats.skew(x)` |
| Curtosis | γ₂ = (1/n) Σ((xᵢ - x̄)/s)⁴ - 3 | `scipy.stats.kurtosis(x, fisher=True)` |

### Coeficiente de Correlación de Pearson

```
r = Σ(xᵢ - x̄)(yᵢ - ȳ) / (√Σ(xᵢ - x̄)² · √Σ(yᵢ - ȳ)²)
```

```python
r, p = scipy.stats.pearsonr(x, y)
```

## Probabilidad

| Concepto | Fórmula |
|----------|---------|
| Probabilidad condicional | P(A\|B) = P(A∩B) / P(B) |
| Probabilidad total | P(A) = Σ P(A\|Bᵢ)·P(Bᵢ) |
| Teorema de Bayes | P(A\|B) = P(B\|A)·P(A) / P(B) |
| Independencia | P(A∩B) = P(A)·P(B) |

## Distribuciones de Probabilidad

| Distribución | Parámetros | Media | Varianza | Python |
|-------------|-----------|-------|----------|--------|
| Bernoulli | p | p | p(1-p) | `stats.bernoulli(p)` |
| Binomial | n, p | np | np(1-p) | `stats.binom(n, p)` |
| Poisson | λ | λ | λ | `stats.poisson(λ)` |
| Normal | μ, σ | μ | σ² | `stats.norm(μ, σ)` |
| t-Student | df | 0 (df>1) | df/(df-2) (df>2) | `stats.t(df)` |
| χ² | df | df | 2df | `stats.chi2(df)` |
| F | df₁, df₂ | df₂/(df₂-2) | - | `stats.f(dfn, dfd)` |
| Exponencial | λ | 1/λ | 1/λ² | `stats.expon(scale=1/λ)` |

## Intervalos de Confianza

| Parámetro | IC (1-α) | Python |
|-----------|----------|--------|
| Media (σ conocida) | x̄ ± z_{α/2}·σ/√n | `stats.norm.ppf(1-α/2)` |
| Media (σ desconocida) | x̄ ± t_{α/2, n-1}·s/√n | `stats.t.ppf(1-α/2, df=n-1)` |
| Proporción (Wilson) | (p̂ + z²/2n ± z√(p̂(1-p̂)/n + z²/4n²)) / (1 + z²/n) | - |
| Diferencia de medias | (x̄₁-x̄₂) ± t_{α/2, ν}·√(s₁²/n₁ + s₂²/n₂) | `stats.ttest_ind(a, b, equal_var=False)` |

## Pruebas de Hipótesis

| Prueba | Estadístico | H₀ rechaza si | Python |
|--------|------------|---------------|--------|
| Z-test 1 muestra | z = (x̄ - μ₀)/(σ/√n) | \|z\| > z_{α/2} | - |
| T-test 1 muestra | t = (x̄ - μ₀)/(s/√n) | \|t\| > t_{α/2, n-1} | `ttest_1samp(datos, popmean)` |
| T-test 2 muestras (indep) | t = (x̄₁-x̄₂)/√(s₁²/n₁+s₂²/n₂) | \|t\| > t_{α/2, ν} | `ttest_ind(a, b, equal_var=False)` |
| T-test pareado | t = d̄/(sd/√n) | \|t\| > t_{α/2, n-1} | `ttest_rel(antes, despues)` |
| ANOVA 1 factor | F = MS_entre/MS_dentro | F > F_{α, k-1, n-k} | `f_oneway(grupo1, grupo2, ...)` |
| Chi-cuadrado | χ² = Σ(O-E)²/E | χ² > χ²_{α, (r-1)(c-1)} | `chi2_contingency(tabla)` |

## Métricas de Modelos

### Regresión

| Métrica | Fórmula | Python |
|---------|---------|--------|
| MAE | (1/n) Σ\|yᵢ - ŷᵢ\| | `mean_absolute_error(y, y_pred)` |
| MSE | (1/n) Σ(yᵢ - ŷᵢ)² | `mean_squared_error(y, y_pred)` |
| RMSE | √MSE | `np.sqrt(mse)` |
| R² | 1 - SS_res/SS_tot | `r2_score(y, y_pred)` |
| MAPE | (100/n) Σ\|yᵢ - ŷᵢ\|/yᵢ | manual |

### Clasificación Binaria

| Métrica | Fórmula | Python |
|---------|---------|--------|
| Accuracy | (TP+TN)/(TP+TN+FP+FN) | `accuracy_score(y, y_pred)` |
| Precisión | TP/(TP+FP) | `precision_score(y, y_pred)` |
| Recall | TP/(TP+FN) | `recall_score(y, y_pred)` |
| F1 | 2·P·R/(P+R) | `f1_score(y, y_pred)` |
| AUC | Área bajo curva ROC | `roc_auc_score(y, y_prob)` |

### Tamaño del Efecto

```
d de Cohen = (x̄₁ - x̄₂) / s_pooled
s_pooled = √(((n₁-1)s₁² + (n₂-1)s₂²) / (n₁ + n₂ - 2))
```

## Fórmulas de Potencia y Tamaño Muestral

### Para Proporción (A/B Testing)

```
n = (z_α · √(2p̄(1-p̄)) + z_β · √(p₁(1-p₁) + p₂(1-p₂)))² / (p₂-p₁)²
```

### Para una Media

```
n = (z_α + z_β)² · σ² / Δ²
```

Donde:
- z_α: valor crítico para α (1.96 para α=0.05)
- z_β: valor crítico para 1-β (0.84 para 80% potencia)
- Δ: diferencia mínima a detectar
