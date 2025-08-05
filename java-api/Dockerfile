FROM eclipse-temurin:17.0.16_8-jdk-jammy AS build
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install dos2unix -y && dos2unix mvnw && chmod +x ./mvnw
RUN ./mvnw package

FROM eclipse-temurin:17.0.16_8-jdk-jammy
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
# Tuning JVM options for better performance
ENV JAVA_OPTS="-XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/app"
# min and max heap size
ENV JAVA_TOOL_OPTIONS="-Xms512m -Xmx2g $JAVA_OPTS"
ENTRYPOINT ["java", "-jar", "app.jar"]