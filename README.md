# A 1.55 μm Wideband 1 × 2 Photonic Power Splitter With Arbitrary Ratio: Characterization and Forward Modeling

## Paper

[A 1.55 μm Wideband 1 × 2 Photonic Power Splitter With Arbitrary Ratio: Characterization and Forward Modeling][Paper]

[Lubaba Tazrian][LT], [Mahmud Elahi Akhter][MEA], [Faizul Rakib Sayem][FRS], [Mainul Hossain][MH], [Rajib Ahmed][RA], [Mirza Mohammad Lutfe Elahi][MLE], [Khaleda Ali][KA] and [Sharnali Islam][SI]


![](./HV_with_TE_TM.png)
## Abstract
Chip-based photonic systems have undergone substantial progress over the last decade. However, the realization of photonic devices still depends largely on intuition-based trial-and-error methods, with a limited focus on characteristic analysis. In this work, we demonstrate an in-depth investigation of photonic power splitters by considering the transmission properties of 16,000 unique ultra-compact silicon-based structures engraved with SiO 2 , Al 2 O 3 , and Si 3 N 4 nanoholes. The characterization has been performed using finite-difference time-domain (FDTD) simulations for each dielectric material and both TE and TM polarizations at the fundamental modes in a wideband optical communication spectrum ranging from 1.45 to 1.65 μm . The corresponding transmissions, splitting ratio, and reflection loss were calculated, generating a dataset that can be used for both forward and inverse modeling purposes, using Machine Learning (ML) and Deep Learning (DL) algorithms. With an optimized hole radius of 35 nm, the proposed device area footprint of 2μm×2μm is among the smallest with the best transmission reported to date. Si 3 N 4 holes show excellent transmission because they offer 90% transmittance in 96% of the data while exhibiting maximum fabrication tolerance. Forward modeling analysis, predicting the transmission properties, was performed using both Linear Model (LM) and Artificial Neural Network (ANN), where LM showed marginally better accuracy than ANN in foreseeing the transmittance. The proposed observation will aid in achieving robust, optimized optical power splitters with a wide range of splitting ratios in lesser time.

## Datasets
The datasets inside TE Mode contain the full dataset. Datasets for all three materials, inside TE Mode have the same hole vector structure but different transmission data. TM Mode datasets only contain the transmission details. We did not provide Holve vector for these as they are the same as TE Mode.   

## Visualization starter code
We have provided a starter code to visualize the hole vector structure of the photonic power splitters. 

### Pre-requisites
* Python 3.6
* pandas
* numpy
* matplotlib

### Running visualization starter
The starter code takes in the desired csv and sample index and outputs a jpg image of the hole vector structure in the provided sample index. The csv file requires to be in the same working directory as the script.

![](./Hole_vector_examples.png) 
```bash
python Visualize.py SiN_TE.csv 50
```
## Forward Neural Network model
We also provide a notebook for our neural netwrok based forward model. 

## Reference

If the code is used in your research, hope you can cite our paper as follows:
```
@ARTICLE{9716852,
  author={Rahman, Lubaba Tazrian and Akhter, Mahmud Elahi and Sayem, Faizul Rakib and Hossain, Mainul and Ahmed, Rajib and Elahi, M. M. Lutfe and Ali, Khaleda and Islam, Sharnali},
  journal={IEEE Access}, 
  title={A 1.55 μm Wideband 1 × 2 Photonic Power Splitter With Arbitrary Ratio: Characterization and Forward Modeling}, 
  year={2022},
  volume={10},
  number={},
  pages={20149-20158},
  doi={10.1109/ACCESS.2022.3151722}}
```
[Paper]: https://ieeexplore.ieee.org/abstract/document/9716852 
[LT]: https://github.com/LTRahman
[MEA]: https://github.com/mandelbrot-walker
[FRS]: https://www.researchgate.net/profile/Faizul-Sayem
[MH]: https://scholar.google.com/citations?user=RLP3qZsAAAAJ&hl=en
[RA]: https://scholar.google.com/citations?user=SmEoIXsAAAAJ&hl=es
[MLE]: https://ece.northsouth.edu/~lutfe.elahi/
[KA]: https://scholar.google.com/citations?user=zDtDMMcAAAAJ&hl=en
[SI]: https://scholar.google.com/citations?user=_FoUlhAAAAAJ&hl=en



