# METHODOLOGY

### ✅ Design Methodologies in Structural Engineering

## 1. **Working Stress Method (WSM)**

Also known as:
- **Elastic Method**
- **Modulus Ratio Method**
- **Factor of Safety Method**

#### 🔹 Key Assumptions & Principles
- Structural materials behave **elastically** under working (service) loads.  
- Stress remains within **permissible limits** using a **factor of safety**.
- Cross-sections are designed such that:  
  **Developed Stress < Permissible Stress**
- Allowable stress lies in the **elastic range**, below the **yield stress**.

#### 🔹 Design Parameters
- **Allowable stress** = `0.6 f_y`
- **Design load (RCC)** = Working/Service load
- **Permissible stress:**  
  \[
  \text{Permissible Stress} = \frac{\text{Characteristic Strength}}{\text{Factor of Safety}}
  \]

**Example (M20 Concrete):**  
- \( f_{ck} = 20 \, \text{MPa} \)

#### 🔹 Factors of Safety

| Material  | Factor of Safety |
|-----------|------------------|
| Concrete  | 3.0              |
| Steel     | 1.78             |

#### 🔹 Additional Notes
- Based on **uniqueness theory** (experience-based).
- Considers the **lower bound theorem**.
- **Serviceability is not addressed** in this method.

---

## 2. **Ultimate Load Method (ULM)**

Also called:
- **Plastic Design Method**
- **Ultimate Load Method**

#### 🔹 Design Load in RCC
\[
\text{Design Load} = \text{Working/Service Load} \times \text{Load Factor}
\]

- Load factor depends on **working conditions**.

#### 🔹 Design Stress
\[
\text{Design Stress} = \frac{\text{Characteristic Strength}}{\text{Factor of Safety}}
\]

#### 🔹 Material Factors of Safety (Beams)

| Material  | Factor of Safety |
|-----------|------------------|
| Concrete  | 1.5              |
| Steel     | 1.15             |

#### 🔹 Theoretical Basis
- **Upper Bound Theorem** → used for determining collapse load  
- **Lower Bound Theorem** → used for material strength  
- **Serviceability not considered**, which reduced usage

---

## 3. **Limit State Method (LSM)**

A modern and advanced philosophy that considers both **safety** and **serviceability**.

#### 🔹 Comparison with Other Methods

| Method                | Basis of Design Load |
|-----------------------|------------------------|
| Working Stress Method | Working (Service) Load |
| Ultimate Load Method  | Ultimate/Collapse Load |
| Limit State Method    | Working Load (for Safety & Serviceability) |

#### 🔹 What is a Limit State?
A **limit state** is the **acceptable threshold** beyond which a structure no longer satisfies safety or serviceability requirements.

---

### ✅ Types of Limit States

#### 🛡️ A. Limit State of Strength
Ensures safety against **structural failure** and **loss of life/property** under worst load combinations.

**Major Types:**
- Loss of equilibrium  
- Loss of stability  
- Excessive deformation or rupture  
- Fatigue fracture  
- Brittle fracture

---

#### 🏠 B. Limit State of Serviceability
Ensures structure performs satisfactorily during its use without discomfort or damage.

#### 🔧 Major Serviceability Criteria

| Type        | Description |
|-------------|-------------|
| **Deflection** | Causes cracks in plaster, damage to finishes, machinery misalignment, reduced strength |
| **Fatigue** | Repeated loading affects bridges, cranes, vibrating structures |
| **Vibration** | Significant in light structures and long spans (e.g., halls, platforms) |
| **Fire Resistance** | Depends on material, geometry, support, and fire protection |
| **Durability** | Ability to function throughout lifespan under expected exposure conditions |

---

#### 🌱 Durability & Sustainability Factors
- Environmental conditions  
- Degree of exposure  
- Shape of members  
- Structural detailing  
- Ease of maintenance  

## Difference between Working Stress Method and Limit State Method

| **Working Stress Method** | **Limit State Method** |
|---------------------------|------------------------|
| It is published in IS: 456 - 1978, 800 – 1984. | It is published in IS: 456 - 2000, 800 – 2007. |
| It is called an Allowable Stress Method (ASM) or Elastic Design Method. | It is also called a Plastic Design Method. |
| Allowable stress is within its range of elastic limit. | Partial Safety Factor (γmo) is used for Yield Stress and Partial Safety Factor (γm1) is used for Ultimate Stress. |
| Analysis of the structure is done by the working load. | Working load is factorized by partial safety factor (YF). Analysis of structure is done by factored load. |
| Working load does not yield or buckle the material. | The behaviour of the material after yield plays an important role in determining the capacity of the material. |
| Deformation is calculated from working load. | Deformation is calculated from the working load. |
| Serviceability and economy not taken into consideration during design. | Serviceability and economy are taken into consideration. |
| It gives heavy design. | It offers lighter sections. |
| Fatigue and fire resistance not taken in calculation. | Fatigue and fire resistance are taken into account. |
