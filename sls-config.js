const path = require("path");
const dotenv = require("dotenv-safe");

let dotenvFileName = ".env.development";
switch (process.env.NODE_ENV) {
  case "production":
    dotenvFileName = ".env.production";
    break;
  case "test":
    dotenvFileName = ".env.test";
    break;
}
dotenv.config({
  path: path.join(__dirname, `${dotenvFileName}`),
});

module.exports = () => {
  config = {
    stage: process.env.NODE_ENV === "production" ? "prod" : "dev",
    logRetentionInDays: process.env.NODE_ENV === "production" ? 30 : 1,
    isProduction: process.env.NODE_ENV === "production" ? 1 : 0,
  };
  return config;
};
