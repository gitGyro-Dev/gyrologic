# Continuity Readability and Identity

## From Local Establishment to Relational Continuity

The preceding section introduced Incorporated Readability as a context update through which distinctions, relations, criteria, and relevance conditions established in one local Gyro realization may become available to later realizations. This update makes later comparison and tracing possible, but it does not by itself establish that two realizations are continuous. A relation may exist without being traceable, and a traceable relation may still fail to become readable as continuity under a given Orientation, Context, and Slice.

Gyro Logic therefore distinguishes at least three levels:

```text
relation existence
≠
traceability
≠
continuity readability
```

This distinction is necessary because continuity is not treated as an intrinsic property automatically carried by two realizations. It is a relational readability that becomes available under specific conditions.

## Local Gyro Realizations

Let a local Gyro realization be represented provisionally as:

\[
g_i=(S_i,B_i,c_i,\Sigma_i,a_i,K_i)
\]

where:

- \(S_i\) is the Structure involved in the realization;
- \(B_i\) is Operator Orientation;
- \(c_i\) is Context;
- \(\Sigma_i\) is the Slice process;
- \(a_i\) is the local articulation made available through Slice;
- \(K_i\) is the corresponding Stability Scene.

This tuple is a bookkeeping schema for formal analysis. It does not imply that every Gyro realization is intrinsically decomposed into six independent objects.

## Relation Existence

Let \(r\) denote a candidate relation between two local realizations \(g_i\) and \(g_j\). We may write:

\[
r(g_i,g_j)
\]

or, more explicitly:

\[
g_i \xrightarrow{r} g_j
\]

The relation \(r\) is intentionally left domain-relative. It may represent, for example:

```text
causal succession
functional succession
semantic inheritance
material transfer
recognized Difference pattern
Boundary correspondence
response-to-orientation linkage
retained readability condition
institutional or rule-based connection
```

The existence of such a relation does not yet imply that it can be traced under the current formal conditions.

## Traceability

Traceability concerns whether the relation can be followed from one realization to another. A provisional predicate is:

\[
\operatorname{Traceable}(g_i,g_j;r)
\]

Traceability may depend on available evidence, incorporated readability, temporal reach, admissible inference rules, or access conditions. A relation may exist while remaining untraceable because the relevant intermediate structure is missing, inaccessible, unreadable, or not yet articulated.

Thus:

\[
r(g_i,g_j)
\not\Rightarrow
\operatorname{Traceable}(g_i,g_j;r)
\]

Traceability is stronger than bare relation existence, but it is still weaker than continuity readability.

## Admissibility

Not every traceable relation should count as a relevant continuity relation. The relation must also be admissible under the Orientation, Context, and Slice used for continuity reading. Let:

\[
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\]

mean that relation \(r\) is admissible relative to Orientation \(B\), Context \(c\), continuity-oriented Slice \(\Sigma\), and incorporated readability context \(\Gamma\).

Admissibility may encode such conditions as:

```text
relevance
scope
permitted inference
causal sufficiency
semantic compatibility
material continuity
institutional validity
temporal accessibility
trust or evidence requirements
```

Admissibility is not assumed to be universal, static, or binary in every domain. It may be graded, defeasible, revisable, or contested.

## Continuity Readability

Continuity Readability is provisionally defined by the conjunction of admissibility, traceability, and readability:

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\]

with the candidate condition:

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\iff
\exists r\,
\Bigl(
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\land
\operatorname{Traceable}(g_i,g_j;r)
\land
\operatorname{Readable}(r;B,c,\Sigma,\Gamma)
\Bigr)
\]

This formula separates three questions:

```text
Is there an admissible relation?
Can it be traced?
Can it be read as continuity here and now?
```

The last condition is essential. A relation may be admissible and traceable, yet not currently readable as continuity because the relevant distinctions, criteria, or contextual organization have not become available.

## Continuity Readability Is Context-Relative

Continuity Readability is not universal across all possible readings. The same pair of realizations may be continuous under one Orientation and discontinuous or indeterminate under another:

\[
\operatorname{CR}(g_i,g_j;B_1,c_1,\Sigma_1,\Gamma_1)
\neq
\operatorname{CR}(g_i,g_j;B_2,c_2,\Sigma_2,\Gamma_2)
\]

This does not mean that continuity is arbitrary. It means that the admissibility and readability of relations depend on explicitly represented conditions.

A later Re-Slice may expose a previously unreadable relation, reject a previously accepted relation, or reorganize the continuity reading. Consequently, Continuity Readability is revisable without being unconstrained.

## Identity as a Separate Criterion

Identity is represented separately from Continuity Readability. Let:

\[
\operatorname{Id}_{q}(g_i,g_j)
\]

mean that \(g_i\) and \(g_j\) are treated as the same entity, bearer, or Structure under identity criterion \(q\).

The criterion \(q\) may concern:

```text
numerical identity
legal identity
functional identity
material persistence
semantic identity
account identity
biological identity
role identity
```

The model does not assume one universal identity criterion.

The central separation is:

\[
\operatorname{CR}(g_i,g_j)
\not\equiv
\operatorname{Id}_{q}(g_i,g_j)
\]

Continuity and Identity answer different questions. Continuity asks whether an admissible relation can be traced and read between realizations. Identity asks whether the realizations are treated as the same under a criterion.

## Continuity Without Identity

The model permits:

\[
\operatorname{CR}(g_i,g_j)=\mathrm{true}
\]

while:

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{false}
\]

For example, batter and cake may be connected through material transformation, causal succession, and production history while not being identical under a type or object criterion. Similarly, a software request and its resulting database update may form a readable continuity relation without being the same entity.

Thus:

```text
Identity break
≠
Trajectory break
```

A change in identity classification does not necessarily destroy relational continuity.

## Identity Without Readable Continuity

The reverse case is also permitted:

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{true}
\]

while:

\[
\operatorname{CR}(g_i,g_j)=\mathrm{false}
\]

or remains indeterminate.

An institution may assert that two records refer to the same legal person even when the continuity between them cannot currently be reconstructed. A system may retain one account identifier even when the behavioral or operational trajectory has become unreadable. Identity claims may therefore survive discontinuity, evidential gaps, or disputed tracing.

## Continuity Readability and Difference

Continuity does not require the absence of Difference. On the contrary, a continuity relation may be readable precisely because a structured pattern of Difference can be traced across realizations.

Let:

\[
\Delta_{B,c,\Sigma}(g_i,g_j)
\]

represent a Slice-relative Difference. Continuity may remain readable when:

\[
\Delta_{B,c,\Sigma}(g_i,g_j)\neq 0
\]

provided that the Difference is admissible within the continuity relation. Therefore:

```text
continuity
≠
unchanged sameness
```

A continuity criterion may incorporate tolerated transformation, bounded deviation, role change, or structured difference.

## Continuity Readability and Incorporated Readability

The context \(\Gamma\) affects which relations are admissible and readable. Earlier Gyro realizations may establish criteria, categories, or inference paths that later enable continuity reading:

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

and subsequently:

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma_{n+1})
\]

may differ from the continuity readability available under \(\Gamma_n\).

This dependence allows retrospective reinterpretation. A relation that was previously unreadable may become traceable and readable after additional distinctions or evidence are incorporated. Conversely, a previously accepted continuity may become invalidated or inaccessible after context revision.

## Binary and Graded Forms

The predicate form of Continuity Readability is useful for the Minimal Formal Model, but some applications may require graded values:

\[
\operatorname{CR}^{*}(g_i,g_j;B,c,\Sigma,\Gamma)
\in \mathcal{C}
\]

where \(\mathcal{C}\) may be an ordered set, confidence interval, evidence structure, or domain-specific classification.

The paper does not require continuity to be universally binary or numerical. The Boolean form expresses only the minimum logical distinction needed for the integrated schema.

## Minimal Commitments

The proposed account commits only to the following:

1. Local Gyro realizations may be related.
2. Relation existence, traceability, admissibility, and readability are distinguishable.
3. Continuity Readability depends on Orientation, Context, Slice, and incorporated readability.
4. Identity is governed by a separate criterion.
5. Continuity may persist through Difference and identity change.
6. Identity may be asserted when continuity is unreadable or disputed.
7. Continuity readings may be revised through Re-Slice and context update.

It does not assume that continuity is an equivalence relation, that it is transitive in every domain, that it is symmetric, that it is globally decidable, or that one identity criterion applies universally.

## Transition to Contextual Trajectory

Continuity Readability concerns whether particular local realizations can be read as connected. A Trajectory requires a broader construction. It involves a family of local realizations, a field of retained relations, and a contextual tracing operation through which a larger relational course becomes readable.

The next section therefore distinguishes the relation-bearing field from the Trajectory itself and develops Trajectory as contextual tracing rather than as a predefined state sequence or chronological log.
