FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /workspace
COPY . .
RUN mvn -ntp -B clean package -DskipTests

FROM eclipse-temurin:17-jammy
WORKDIR /app
COPY --from=build /workspace/target/mcp-oauth2-demo-*.jar app.jar
EXPOSE 8081
ENTRYPOINT ["java","-jar","/app/app.jar"]
