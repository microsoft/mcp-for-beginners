FROM eclipse-temurin:17-jammy AS build
WORKDIR /workspace
COPY . .
RUN ./mvnw -ntp -B clean package -DskipTests

FROM eclipse-temurin:17-jammy
WORKDIR /app
COPY --from=build /workspace/target/mcp-oauth2-demo-*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","/app/app.jar"]
