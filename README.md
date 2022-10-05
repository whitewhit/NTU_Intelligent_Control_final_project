# Final Project

## 1. <font color=#FF6600> Final Project Proposal by Fuzzy Logic</font>

應用模糊控制於魚塭增氧機

### 1.動機

>1.我國養殖漁業具有龐大的經濟價值  
![養殖漁業產值](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20003238.png)  
>2.以養殖魚業賴以為生的魚戶達3萬餘戶，面積也達4萬多公頃

    1.我國養殖漁業具有龐大的經濟價值
    2.以養殖魚業賴以為生的魚戶達3萬餘戶，面積也達4萬多公頃

為了要降低生產成本以及確保養殖漁的矬活率與品質，水中溶氧量詹句了重要的因素，此外溶氧度也可以反映出水體受汙染的程度，因此也是衡量水質的重要指標

### 2.方法

我們希望能藉由溫度、壓力等簡單易量測且價格相對較便宜的感測器，運用這學期學到的模糊控制理論，確保溶氧量在最佳範圍內，且能控制打氧機運行的時間，達到節能的效果。

因此，本次期末專題我們嘗試利用模糊控制的架構以四個輸入函數分別為:

+ 1. 溫度(︒C) : 溫度越高，水中 溶氧量越低  
+ 2. 平均每台增氧機負荷面積(m^2/台)  
+ 3. 大氣壓力(hPa) : 大氣壓力越高，水中溶氧量越高
+ 4. 魚群飼養密度(kg/m^3) : 因為魚群會隨時間成長，因此此項會根據飼養時間推測其平均重量來更改輸入  
  
![系統示意圖](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20003859.png)

#### 輸入函數

+ 1.溫度分成三個等級:  
  + Cold : 5~22(︒C)  
  + Normal : 12~32 (︒C)  
  + Hot : 22~40(︒C)  
![溫度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20011041.png)
+ 2.增氧機負荷面積分成三個等級:  
  + small : 1500~3200 (m^2/台)  
  + normal : 2200~4300 (m^2/台)  
  + big : 3200~5000 (m^2/台)  
![負荷面積](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20011052.png)
+ 3.大氣壓力分為三個等級:  
  + small :Low:990~1013  (hPa)  
  + normal : normal:1003~1023 (hPa)  
  + big : high:1013~1030 (hPa)  
![大氣壓力](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20011102.png)
+ 4.飼養密度分為三個等級:  
  + low:0.3~1.3(kg/m^3)  
  + normal:0.9~1.7 (kg/m^3)  
  + high:1.3~2.3 (kg/m^3)  
![飼養密度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20011110.png)

#### 輸出函數

輸出則由打氧機最佳的運作時間來呈現

+ 運作時間分成五個等級:
  + shortest :60~90(min)
  + shorter:80~110(min)
  + medium:100~140(min)
  + longer:120~180(min)
  + longest:150~180(min)
![時間](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20011819.png))

#### 規則

| | temp | pressure | density | area |
| -------- | -------- | -------- | -------- | -------- |
| <font color=#008000>G</font> : 減少運作時間的條件: | low | high | low | small |
| <font color=#0000FF>B</font> : 增加運作時間的條件: | high | low | high | big |
| <font color=#800000>N</font>: 普通的條件:| normal | normal | normal | normal |

#### 組合數

|條件組合|數量|條件組合|數量|
| -------- | -------- | -------- | -------- |
| 4<font color=#0000FF>B</font> | 1 | 1<font color=#0000FF>B</font>3<font color=#800000>N</font> | 4 |
| 4<font color=#008000>G</font> | 1 | 3<font color=#008000>G</font>1<font color=#800000>N</font> | 4 |
| 4<font color=#800000>N</font> | 1 | 2<font color=#008000>G</font>2<font color=#800000>N</font> | 6 |
| 3<font color=#0000FF>B</font>1<font color=#008000>G</font> | 4 | 1<font color=#008000>G</font>3<font color=#800000>N</font> | 4 |
| 3<font color=#0000FF>B</font>1<font color=#800000>N</font> | 4 | 2<font color=#0000FF>B</font>2<font color=#008000>G</font>1<font color=#800000>N</font> | 12 |
| 2<font color=#0000FF>B</font>2<font color=#008000>G</font> | 6 | 1<font color=#0000FF>B</font>2<font color=#008000>G</font>1<font color=#800000>N</font> | 12 |
| 2<font color=#0000FF>B</font><font color=#800000>N</font> | 6 | 1<font color=#0000FF>B</font>1<font color=#008000>G</font>2<font color=#800000>N</font> | 12 |
| 1<font color=#0000FF>B</font>3<font color=#008000>G</font> | 4 |  |  |

#### 假設

因為時間的因素，以及數據的缺乏，因此假設四項因素對溶氧量的影響程度皆相同，所以只要字母出現的次數皆相同，都會被歸類為同一個輸出函數。
未來如果有更多時間以及充足的數據做補充，將視情況做調整。

#### 規則分佈

+ 1.先將一些obvious rules像是4G、4B、4N…等決定
+ 2.將其餘的規則以最多出現的英文字母以及類似權重的概念(訂G=1，N=0，B=-1)加   權，再將全部四個英文字母相加後得到一個情況下rule的數值來考量

#### 輸出結果

如果將所有輸入及輸出一次全部畫在圖上時，結果圖會是一張五維圖，不好觀察出關係，而且也十分的不直觀。因此在表示地方面，我們決定先任選其中兩項因素並固定其數值，這樣畫出的關係圖會是三維圖，比較直觀。

+ ![固定飼養密度、增氧機負荷面積](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014223.png)
+ ![固定溫度、負荷面積](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014257.png)  
![固定溫度、負荷面積](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014306.png)
+ ![固定氣壓、溫度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014315.png)  
![固定氣壓、溫度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014324.png)
+ ![固定氣壓、飼養密度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014337.png)  
![固定氣壓、飼養密度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014411.png)  
+ ![固定負荷面積、氣壓](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014425.png)
+ ![溫度、飼養密度](https://github.com/whitewhit/NTU_Intelligent_Control_final_project/blob/main/fuzzy%E5%9C%96%E7%89%87/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202022-10-06%20014436.png)

#### 結果討論

由於我們缺乏真實世界中的相關數據，因此我們就僅觀察輸出函數的合理性，
像是圖形有無明顯的上下起伏並且已漸增的方式向一個方向分布來進行討論，
從上方的測試結果可發現圖形是可以接受的，雖然部分的狀態的圖形會有稍微
凹凸不平的情形出現。那就可能跟我們的輸入規則會有關，例如說可能同樣是
2G1N1B，輸出的函數要不同，以及其實不用那麼多輸入規則。

#### 未來期許

因為時間緊湊以及缺乏真實資料的佐證，因此我們並未能對各個輸入的因素做出不同程度的比重，感到有些許的遺憾。
未來如果有更多上述因素對溶氧量影響程度的資料時，將資料導入至此系統，我相信此系統有機會可以實際運用於實際的養殖漁業中，保持養殖漁業魚類的品質以及避免打氧機過度運作耗能。


## Final Project Proposal by Artificial Neural Network (ANN)

應用CNN於花朵類別判別

### 動機

有鑑於台灣地區地貌豐富花卉種類繁多，且台灣為輸出蘭花的大國，「花卉王國」的美稱，因此希望製作出可以依據花瓣形狀、數量跟顏色等特徵分辨出花卉種類的程式。希望藉由此程式帶領大家認識花卉，並對各種花卉有更進一步的了解
![花卉中值面積與產值]()

### 方法

+ 1.找出台灣常見花卉照片10種各100張(目前想要找的花卉為: 梅花、櫻花、桐花、百合花、蓮花、金針花、木棉花、繡球花、蘭花、桂花)
+ 2.將上述照片運用CNN技術分類
![CNN]()
+ 3.建立王CNN網路之後，輸入各類花卉圖片，並顯示出該圖花卉種類

### 預期的結果

希望製作出能用手機鏡頭對準該花卉後，就能分析出花卉種類並將該花卉詳細介紹的應用程式，幫助大眾瞭解花的種類

