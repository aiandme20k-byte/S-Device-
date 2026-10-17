plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}
android {
    namespace = "org.sdevice.mobile"
    compileSdk = 35
    defaultConfig {
        applicationId = "org.sdevice.mobile"
        minSdk = 26
        targetSdk = 35
        versionCode = 2
        versionName = "0.2.0"
    }
}
