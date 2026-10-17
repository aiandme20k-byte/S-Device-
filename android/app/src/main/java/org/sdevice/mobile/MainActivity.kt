package org.sdevice.mobile

import android.app.Activity
import android.content.ActivityNotFoundException
import android.content.Intent
import android.graphics.Color
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.Uri
import android.os.Bundle
import android.telephony.TelephonyManager
import android.view.Gravity
import android.widget.Button
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView

/**
 * Build 011: SIM and active transport read-only diagnostics.
 * Cellular calls/SMS remain handled by the phone's certified Android OS and dialer.
 * No phone numbers, IMEI or SIM IDs are read or uploaded.
 */
class MainActivity : Activity() {
    private lateinit var status: TextView
    private lateinit var cm: ConnectivityManager
    private var monitoring = false
    private val callback = object : ConnectivityManager.NetworkCallback() {
        override fun onAvailable(network: Network) = refreshOnUiThread()
        override fun onLost(network: Network) = refreshOnUiThread()
        override fun onCapabilitiesChanged(network: Network, caps: NetworkCapabilities) =
            refreshOnUiThread()
    }

    private fun refreshOnUiThread() = runOnUiThread { updateNetworkStatus() }

    private fun action(text: String, parent: LinearLayout, handler: () -> Unit) {
        val b = Button(this).apply {
            this.text = text
            textSize = 16f
            setTextColor(Color.WHITE)
            setBackgroundColor(Color.rgb(20, 74, 108))
            setOnClickListener { handler() }
        }
        parent.addView(b, LinearLayout.LayoutParams(-1, -2).apply {
            topMargin = 10
            bottomMargin = 4
        })
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        cm = getSystemService(CONNECTIVITY_SERVICE) as ConnectivityManager
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(24, 36, 24, 30)
            setBackgroundColor(Color.rgb(7, 20, 38))
        }
        fun label(text: String, size: Float, color: Int): TextView {
            return TextView(this).apply {
                this.text = text
                textSize = size
                setTextColor(color)
                gravity = Gravity.CENTER_HORIZONTAL
                setPadding(0, 10, 0, 10)
                root.addView(this)
            }
        }
        label("QVE HNS • FUTURE TECHNOLOGY", 16f, Color.rgb(216, 182, 108))
        label("S DEVICE", 38f, Color.rgb(93, 220, 255))
        label("QUANTUM • VISION • EXPLORATION", 12f, Color.rgb(216, 182, 108))
        label("Android-based S Device Experience • Build 011", 15f, Color.WHITE)
        label("SIM • MOBILE DATA • VOICE • SMS", 17f, Color.rgb(93, 220, 255))
        status = label("Checking network…", 16f, Color.WHITE)
        action("Refresh SIM & Network", root) { updateNetworkStatus() }
        action("Open Phone Dialer", root) {
            try { startActivity(Intent(Intent.ACTION_DIAL)) }
            catch (_: ActivityNotFoundException) { status.text = "Phone dialer unavailable" }
        }
        action("Open SMS", root) {
            try { startActivity(Intent(Intent.ACTION_SENDTO, Uri.parse("smsto:"))) }
            catch (_: ActivityNotFoundException) { status.text = "SMS app unavailable" }
        }
        label("Cellular service requires a working SIM, plan and carrier coverage. Network status is local-only. Private AI server pairing is not enabled.", 13f, Color.LTGRAY)
        label("Authorized By SETT", 13f, Color.rgb(216, 182, 108))
        label("EXPLORE • ENGINEER • CREATE • A BETTER TOMORROW", 11f, Color.GRAY)
        setContentView(ScrollView(this).apply { addView(root) })
        updateNetworkStatus()
    }

    override fun onStart() {
        super.onStart()
        try {
            cm.registerDefaultNetworkCallback(callback)
            monitoring = true
        } catch (_: SecurityException) {
            monitoring = false
            updateNetworkStatus()
        }
    }

    override fun onStop() {
        if (monitoring) {
            try { cm.unregisterNetworkCallback(callback) }
            catch (_: IllegalArgumentException) { }
            monitoring = false
        }
        super.onStop()
    }

    private fun updateNetworkStatus() {
        val sim = try {
            val telephony = getSystemService(TELEPHONY_SERVICE) as TelephonyManager
            when (telephony.simState) {
                TelephonyManager.SIM_STATE_READY -> "READY"
                TelephonyManager.SIM_STATE_ABSENT -> "ABSENT"
                TelephonyManager.SIM_STATE_PIN_REQUIRED -> "PIN REQUIRED"
                TelephonyManager.SIM_STATE_PUK_REQUIRED -> "PUK REQUIRED"
                TelephonyManager.SIM_STATE_NETWORK_LOCKED -> "NETWORK LOCKED"
                else -> "UNKNOWN / INITIALIZING"
            }
        } catch (_: SecurityException) { "UNAVAILABLE (permission)" }
        val caps = cm.getNetworkCapabilities(cm.activeNetwork)
        val transport = when {
            caps == null -> "NO ACTIVE NETWORK"
            caps.hasTransport(NetworkCapabilities.TRANSPORT_WIFI) -> "WI-FI"
            caps.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR) -> "CELLULAR DATA"
            caps.hasTransport(NetworkCapabilities.TRANSPORT_ETHERNET) -> "ETHERNET"
            else -> "OTHER NETWORK"
        }
        val validation = when {
            caps == null -> "OFFLINE"
            caps.hasCapability(NetworkCapabilities.NET_CAPABILITY_VALIDATED) -> "ANDROID-VALIDATED INTERNET"
            caps.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET) -> "INTERNET CAPABILITY (NOT VALIDATED)"
            else -> "LOCAL NETWORK ONLY"
        }
        status.text = "SIM: $sim\nActive transport: $transport\nConnectivity: $validation\n\nSIM/phone status is read-only. No data or calls are sent by S Device."
    }
}
