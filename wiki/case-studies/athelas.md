---
title: Athelas
type: case-study
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["Athelas"]
related: ["[[Hard Tech Startups]]", "[[University Spinouts]]"]
sources: ["4x-on-starting-a-company-from-a-hackathon-project"]
speakers_referenced: ["Tanay Tandon"]
---

# Athelas

Athelas (YC S16) makes low-cost devices that enable rapid blood diagnostics through computer vision. The company was founded by Tanay Tandon and his co-founder Deepika. It started as a proof-of-concept built overnight at [YC Hacks 2014](https://ychacks.devpost.com/submissions/25781-athelas) and grew into a shippable medical product [1].

## From Hackathon to Product

[![Athelas hackathon prototype](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/dc4f11da762d.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-1.png)

The first version used a rubber piece and spherical magnifier attached to a smartphone camera. A blood sample was held (by a toilet paper roll) underneath, the camera took images, and computer vision rendered malaria cell counts. The design was similar to a [van Leeuwenhoek microscope](https://en.wikipedia.org/wiki/Antonie_van_Leeuwenhoek) -- one of the earliest microscopes built, used to see microorganisms for the first time [1].

[![Athelas cell classification](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/21b8f50e25a9.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-2.png)

[![Athelas cell segmentation](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/393ab971f08b.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-4.png)

[![Athelas cell recognition output](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/df9dcd053523.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-5.png)

The hackathon focused on segmentation and template matching combined with a fast random forest model that classified extracted Red Blood Cells. Cell boundaries were recognized, then fed into the classifier to identify parasitic cells like Malaria or Trypanosoma [1].

"While functioning and a neat trick, someone needed to be physically holding the camera in place, the slide had to be moved around, with the lighting often being hard to fix. At the end of the day it was a nice experimental toy you might see someone post as a video on Facebook" [1].

## Technical Evolution

Turning the demo into a product required advances on multiple fronts [1]:

[![Athelas hardware evolution](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/eb2bd58bdaed.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-6.png)

**Hardware**: Higher-resolution optics in a standalone, cheap device with actuation systems and Gaussian edge autofocusing algorithms for consistent cell capture.

**Sample preparation**: Deepika perfected a fast staining mechanism, synthesizing dozens of stain compound versions and coating them on plastic strips for out-of-the-box use. The strip needed to create a "monolayer" (single layer of cells) for statistically representative imaging.

**Computer vision**: Training data assembled from public CDC images and blood smears collected from researchers at Stanford and UCSF, often hand-labeled by Tandon or a pathologist. Traditional computer vision and deep learning approaches classified cell types.

[![Athelas deep learning classification](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/d27965e1b0d8.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-7.png)

[![Athelas training data](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/4daccd321fda.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-8.png)

## Clinical Validation

During YC (full-time, summer batch), clinical validation was conducted locally and at the FEMAP family hospital. The goal: prove the system on White Blood Cell counts. Results across 350 patients showed high-accuracy correlation with the gold-standard Beckman Counter [1].

Athelas's computer vision approach has an advantage over traditional Coulter counting. Coulter counters flow particles through a jeweled aperture and record impedance to classify by particle size. Particulate matter or lymph can confuse a Coulter system, especially in diluted quantities. Athelas's vision classifies such artifacts as non-leukocyte cellular bodies, avoiding false counts [1].

The trial showed 100% 5-class inter-rater agreement between the two systems. Data was submitted to the FDA for Class 2 510(k) approval, and distribution began for the Class 1 version [1].

[![Athelas clinical validation results](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/6ae9b7460c81.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-13.png)

[![Athelas final product](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/104f634a1e0c.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-14.png)

[![Athelas device and app](../raw/posts/images/4x-on-starting-a-company-from-a-hackathon-project/e9768e42baba.png)](https://blog.ycombinator.com/wp-content/uploads/2017/01/athelas-15.png)

## Challenges

Progress was slow before YC. College workload at Stanford combined with rising hardware iteration costs made consistent progress difficult. "Finals often meant days going by without any tangible progress whatsoever" [1]. Going from hackathon prototype to shippable product was "a progression in dimensionality at every stage" [1].

The devices shipped at $250 for point-of-care locations, homes, and clinical settings, with plans to integrate concussion monitoring, inflammation tracking, urinary tract infection detection, platelets, and additional cell counts [1].

## References

1. [On Starting a Company from a Hackathon Project](https://www.ycombinator.com/library/4x-on-starting-a-company-from-a-hackathon-project) -- Tanay Tandon (January 2017)
