from typing import Literal
from pydantic import model_validator, Field, EmailStr, BaseModel, ValidationError, HttpUrl


class AppConfig(BaseModel):
    app_name:str = Field(default = "PlaywrightAutomation")
    environment:Literal["development", "staging", "production"]
    timeoutSeconds: int = Field(default = 30, ge=1)
    baseUrl: HttpUrl
    retry_attempts: int = Field(default = 3)

    @model_validator(mode="after")
    def check_env(self):
        if self.environment == "production" and self.retry_attempts<3:
            raise ValueError("Production environment requires at least 3 retry attempts")

        return self

def main():

    try:
        config1 = AppConfig(
            environment = 'production',
            timeoutSeconds = 4,
            baseUrl = "https://prodtest.com",
            retry_attempts = 5
        )
        print("CONFIG 1 SUCCESS", config1)
    except ValidationError as e:
        print("Config 1 error", e)

    try:
        config2 = AppConfig(
            environment = 'production',
            timeoutSeconds = 4,
            baseUrl = "https://prodtest.com",
            retry_attempts = 2
        )
        print("CONFIG 2 SUCCESS", config2)
    except ValidationError as e:
        print("Config 2 error", e)


if __name__ == "__main__":
    main()


    