# CyberSanity Data Sheet

Single source of truth for every number in the project. If a value changes, tell the whole group and recalculate the test table.

## 1. Cybernetic components

Tuple order in code: `(name, slot, humanity_loss, power_draw, category)`

| # | Component | Slot | Humanity loss | Power (W) | Category |
|---|---|---|---|---|---|
| 1 | Optical Scanner | Eyes | 5 | 10 | Civilian |
| 2 | Subdermal Armor | Skin | 10 | 20 | Civilian |
| 3 | Load-Lifter Arm | Arm | 12 | 40 | Industrial |
| 4 | Kerenzikov | Nervous | 15 | 30 | Combat |
| 5 | Mantis Blades | Arm | 18 | 35 | Combat |
| 6 | Sandevistan | Nervous | 25 | 60 | Combat |
| 7 | Neural Link | Nervous | 20 | 50 | Combat |
| 8 | Prosthetic Arm | Arm | 8 | 25 | Medical |
| 9 | Retinal Implant | Eyes | 6 | 12 | Medical |
| 10 | Smart Wrist Display | Arm | 3 | 5 | Civilian |
| 11 | Night Vision Lens | Eyes | 7 | 15 | Civilian |
| 12 | Heavy Grip Hand | Arm | 10 | 30 | Industrial |

Items 10 to 12 are optional extras that let Citizen and Worker users show slot clashes.

Body slots: Eyes, Skin, Arm, Nervous

Humanity loss tiers (for the proposal explanation):

| Tier | Range | Rule |
|---|---|---|
| Low | 1 to 7 | Sensory or minor add-on |
| Medium | 8 to 14 | Replaces a body part, or embedded under the skin |
| High | 15 to 25 | Nervous system link, or combat-grade |

## 2. User types

| # | User | Power Core capacity | Allowed categories | Humanity modifier |
|---|---|---|---|---|
| 1 | Citizen | 100 W | Civilian | 1.0 |
| 2 | Worker | 150 W | Civilian, Industrial | 1.0 |
| 3 | Military | 250 W | Civilian, Industrial, Combat | 0.8 |
| 4 | Disabled | 100 W | Civilian, Medical | 0.5 for Medical parts, 1.0 for the rest |

## 3. Constants

| Item | Value |
|---|---|
| Starting Humanity Index | 100 |
| Power Load cap | 100 % |
| Compatibility Penalty per slot clash | 25 |
| Compatibility Penalty cap | 100 |
| Overload weights | Power Load 0.4, Humanity Loss 0.3, Penalty 0.3 |
| Overload alert level | above 75 |
| Malfunction chance per hour | Overload Risk Score minus 70 (%) |
| Malfunction simulated hours | up to 24 |

## 4. Formulas

- Adjusted loss = base humanity loss x user modifier
- Humanity Index = 100 - total adjusted loss
- Power Load % = total power draw / capacity x 100 (capped at 100)
- Slot clashes = for each slot, (number of installed parts in it) - 1, if more than 1
- Compatibility Penalty = 25 x slot clashes (capped at 100)
- Overload Risk Score = 0.4 x Power Load % + 0.3 x (100 - Humanity Index) + 0.3 x Compatibility Penalty

## 5. Status levels

| Humanity Index | Status | Dampener Advisory |
|---|---|---|
| 70 to 100 | Stable | None required |
| 40 to 69 | Warning | Light: avoid installing further components |
| 20 to 39 | Cyberpsychosis Risk | Strong: remove components until HI is 40 or higher |
| Below 20 | Critical | Maximum: installation locked, remove components immediately |

If the Overload Risk Score is above 75, Stable or Warning is raised to Cyberpsychosis Risk. Critical is never lowered.

Status words must be spelled exactly: Stable, Warning, Cyberpsychosis Risk, Critical.

## 6. Test table (Military, 250 W, modifier 0.8)

| Setup | HI | Power | Penalty | Score | Status |
|---|---|---|---|---|---|
| Mantis Blades, Kerenzikov, Sandevistan | 53.6 | 50% | 25 | 41.4 | Warning |
| Add Optical Scanner, Subdermal Armor, Load-Lifter Arm | 32 | 78% | 50 | 66.6 | Cyberpsychosis Risk |
| Add Neural Link too | 16 | 98% | 75 | 86.9 | Critical |
| Second setup, Sandevistan removed | 36 | 74% | 50 | 63.8 | Cyberpsychosis Risk |
