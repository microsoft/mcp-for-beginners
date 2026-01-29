# Calculator HTTP Streaming Demo

此專案示範如何使用 Spring Boot WebFlux 透過 Server-Sent Events (SSE) 實現 HTTP 串流。專案包含兩個應用程式：

- **Calculator Server**：一個反應式網路服務，執行計算並使用 SSE 串流結果
- **Calculator Client**：一個客戶端應用程式，消費串流端點

## 先決條件

- Java 17 或以上版本
- Maven 3.6 或以上版本

## 專案結構

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## 運作原理

1. **Calculator Server** 提供 `/calculate` 端點，功能如下：
   - 接收查詢參數：`a`（數字）、`b`（數字）、`op`（運算）
   - 支援的運算：`add`、`sub`、`mul`、`div`
   - 回傳包含計算進度與結果的 Server-Sent Events

2. **Calculator Client** 連接伺服器並：
   - 發送請求計算 `7 * 5`
   - 消費串流回應
   - 將每個事件輸出到主控台

## 執行應用程式

### 選項 1：使用 Maven（推薦）

#### 1. 啟動 Calculator Server

打開終端機並切換到伺服器目錄：

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

伺服器將在 `http://localhost:8080` 啟動

你會看到類似以下的輸出：
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. 執行 Calculator Client

打開**新的終端機**並切換到客戶端目錄：

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

客戶端會連接伺服器，執行計算並顯示串流結果。

### 選項 2：直接使用 Java

#### 1. 編譯並執行伺服器：

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. 編譯並執行客戶端：

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## 手動測試伺服器

你也可以使用瀏覽器或 curl 測試伺服器：

### 使用瀏覽器：
造訪：`http://localhost:8080/calculate?a=10&b=5&op=add`

### 使用 curl：
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## 預期輸出

執行客戶端時，你應該會看到類似以下的串流輸出：

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## 支援的運算

- `add` - 加法 (a + b)
- `sub` - 減法 (a - b)
- `mul` - 乘法 (a * b)
- `div` - 除法 (a / b，若 b = 0 則回傳 NaN)

## API 參考

### GET /calculate

**參數：**
- `a`（必填）：第一個數字（double）
- `b`（必填）：第二個數字（double）
- `op`（必填）：運算類型（`add`、`sub`、`mul`、`div`）

**回應：**
- Content-Type: `text/event-stream`
- 回傳包含計算進度與結果的 Server-Sent Events

**範例請求：**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**範例回應：**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## 疑難排解

### 常見問題

1. **埠號 8080 已被使用**
   - 停止其他使用 8080 埠號的應用程式
   - 或修改 `calculator-server/src/main/resources/application.yml` 中的伺服器埠號

2. **連線被拒絕**
   - 確認伺服器已啟動，且在埠號 8080 正常運作
   - 確保在啟動客戶端前伺服器已啟動

3. **參數名稱問題**
   - 專案包含 Maven 編譯器設定，使用 `-parameters` 旗標
   - 若遇到參數綁定問題，請確認專案已使用此設定編譯

### 停止應用程式

- 在執行應用程式的終端機按下 `Ctrl+C`
- 或若以背景程序執行，使用 `mvn spring-boot:stop`

## 技術棧

- **Spring Boot 3.3.1** - 應用程式框架
- **Spring WebFlux** - 反應式網路框架
- **Project Reactor** - 反應式串流函式庫
- **Netty** - 非阻塞 I/O 伺服器
- **Maven** - 建置工具
- **Java 17+** - 程式語言

## 下一步

嘗試修改程式碼以：
- 新增更多數學運算
- 加入無效運算的錯誤處理
- 新增請求/回應日誌
- 實作身份驗證
- 新增單元測試

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。