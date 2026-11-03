FROM maven:3.9.16-eclipse-temurin-21-noble AS build
WORKDIR /workspace
COPY . .
RUN mvn -ntp -B clean package -DskipTests

FROM eclipse-temurin:21.0.13_9-jre-noble
WORKDIR /app
COPY --from=build /workspace/target/mcp-oauth2-demo-*.jar app.jar
EXPOSE 8081
ENTRYPOINT ["java","-jar","/app/app.jar"]
