---
layout: default
title: Privacy Policy
permalink: /privacy_policy_en.html
---

# Sabiowl Privacy Policy

<p style="color: #666; font-size: 0.9em;">Last updated: 2 August 2026</p>

---

## Article 1 (Scope)

This Privacy Policy sets out how Sabiowl (the "Service") handles users' personal
information and usage information.

---

## Article 2 (Information we collect)

The Service may collect the following information.

### Basic information
- The name (nickname) you enter
- Gender (optional; you may decline to answer)
- Authentication identifiers linked from your Google or Apple account (email
  address, display name, provider-side UID)

### In-app data
- Data created within the Service, such as habits, to-dos, timeline entries, and
  characters
- Habit completion records and game progress such as level, experience points,
  and stats
- Gacha history and owned item information

### Linked calendar data (only when Google Calendar integration is enabled; import only in v1.0)
- Event information imported from Google Calendar (title, date and time, notes)

### Device information
- OS version, app version, device model
- Push notification token (FCM token)

### Diagnostic and support data
- **Diagnostic data**: crash logs (stack traces of uncaught exceptions in Flutter
  and Django, and the app state at the time) and performance data (statistics on
  screen rendering speed and API response times, sampled at 10%). **Personally
  identifying information is removed automatically before collection**, and this
  data is not used for third-party tracking.
- **Contact form messages and attached images** (up to 5 files, 10MB in total).
  These are stored together with your email address so that we can reply, and are
  kept for one year after the enquiry is resolved.

### Voice input (Quick Notes feature, v1.0.4 and later)
- Audio captured by the microphone is converted to text by the speech recognition
  function provided by your device's operating system (iOS: Apple speech
  recognition / Android: the device's speech recognition service). **Our servers
  never receive the audio itself.**
- The converted text is stored on our servers as a note only if you choose to save
  it (this falls within the scope already described under "In-app data").
- Whether speech recognition is completed entirely on your device or goes through
  the OS provider's servers depends on your device, OS version, and language
  settings. Please refer to the privacy policy of your OS provider for details.

---

## Article 3 (Purposes of use)

We use the information we collect for the following purposes.

- Providing and improving the Service
- Responding to defects and enquiries
- Statistical analysis aimed at improving the user experience
- Sending replies to enquiries (email delivery)
- Delivering push notifications (important announcements, friend features, etc.)
- Synchronising data with linked calendar services

---

## Article 4 (Provision to third parties)

We do not provide your personal information to third parties without your consent.
This does not apply where disclosure is required by law, or to the limited display
of information that occurs when you use the Service's friend feature (see Article
4-2).

---

## Article 4-2 (Information sharing in the friend feature)

If you use the Service's friend feature, only the following information is visible
to other users whom you have approved as friends.

### Visible to friends
- User name
- Current level
- Currently selected character
- Habit streak length (best_streak)

### Not visible to friends
- Habit names, contents, or categories
- Monthly completion rate
- Individual completion logs or history
- Contact enquiry contents

The Service never shares the actual contents of your habits with other users,
including friends. The motivational aspect of the friend feature is built solely
on streak length, a number that reveals nothing about what you are doing.

---

## Article 5 (Use of analytics tools)

To improve the Service, we use "PostHog", a third-party product analytics tool
provided by PostHog Inc. PostHog uses cookies and similar technologies to measure
usage of the Service anonymously.

### Information collected
- In-app screen transitions and interaction events (taps, button presses, etc.)
- Device information (OS, app version, device model)
- An internal identifier (a value derived from the PlayerProfile ID)

### Information not collected
- Your email address
- Your name or nickname
- Confidential information such as authentication tokens or passwords

### Where the data is stored
PostHog Cloud (US region: `https://us.i.posthog.com`).

### Purposes
- Understanding how features are used
- Improving the user experience
- Identifying and fixing defects

### Deletion
When you delete your account, the corresponding data in PostHog is deleted
automatically. You may also contact us to request individual deletion.

### Further information
See PostHog's privacy policy at [https://posthog.com/privacy](https://posthog.com/privacy).

---

## Article 6 (Crash and performance monitoring: Sentry)

To improve app quality, we use the crash monitoring and performance measurement
SDK provided by Sentry (operated by Functional Software, Inc., United States).

### Information collected
- Stack traces and snapshots of app state at the time of a crash
- Statistical data on screen rendering speed and API response times

### Purposes
- Early detection of defects and quality improvement

### Handling of personal information
A `beforeSend` hook in the SDK automatically removes user-identifying information
(email address, PlayerProfile ID, name, device-specific identifiers) before
transmission. On the Sentry dashboard we review crashes **by occurrence, not by
device**. For details of personal data scrubbing, see
[https://docs.sentry.io/platforms/flutter/enriching-events/scrubbing/](https://docs.sentry.io/platforms/flutter/enriching-events/scrubbing/).

### Where the data is stored
Sentry Cloud (US region).

### Further information
See Sentry's privacy policy at [https://sentry.io/privacy/](https://sentry.io/privacy/)
and its data processing terms at [https://sentry.io/legal/dpa/](https://sentry.io/legal/dpa/).

---

## Article 7 (Authentication service: Firebase Authentication)

We use "Firebase Authentication", provided by Google, to authenticate users.

### How we use it
- Sign-in with a Google or Apple account
- Maintaining your signed-in state
- Passwordless authentication (via OAuth providers)

### Information sent to Firebase Authentication
- Credentials from the OAuth provider used to sign in (Google or Apple)
- Your email address (obtained from the OAuth provider)
- The provider-side UID

### Where the data is stored
Google Cloud (Firebase services).

### Deletion
When you delete your account, we also delete the corresponding user record in
Firebase Authentication automatically.

### Further information
See Firebase's privacy policy at
[https://firebase.google.com/support/privacy](https://firebase.google.com/support/privacy).

---

## Article 8 (Push notifications: Firebase Cloud Messaging)

We use "Firebase Cloud Messaging (FCM)", provided by Google, to deliver push
notifications.

### How we use it
- Delivering notifications such as friend requests, received messages, and habit
  reminders
- Delivering important announcements within the Service

### Information sent to FCM
- The device token used for delivery (FCM token)
- Notification body, title, and related metadata

### Turning notifications off
You can disable push notifications in your device's OS settings.

### Further information
See Firebase's privacy policy at
[https://firebase.google.com/support/privacy](https://firebase.google.com/support/privacy).

---

## Article 9 (Google Calendar integration)

The Service offers one-way synchronisation that imports events from Google
Calendar into the Service. Using it requires your explicit consent (enabling
"Google Calendar integration" in Settings, and running "Sync Google Calendar" from
the calendar screen).

### Change of policy from v1.0 (29 May 2026)
The previously offered "automatic reflection from the Service into Google Calendar"
(two-way synchronisation) was discontinued with the v1.0 release. Events you create
in the Service are never written to Google Calendar. Import from Google Calendar
into the Service continues to be offered.

### Google API scopes used
- `https://www.googleapis.com/auth/calendar.events`
  In v1.0 this is used for import (reading) only. The scope technically includes
  write permission, but write API calls from the Service are structurally blocked
  (`FeatureFlags.gcalPushEnabled = false`).

### Information obtained
- Events on your Google Calendar (title, date and time, notes, identifier)

### Your control
- You can start an import manually by running "Sync Google Calendar" from the menu
  on the calendar screen. No automatic import takes place.
- The "Disconnect Google Calendar" button deletes the imported Google-originated
  data and stops any further integration.

### Where the data is stored
The body of imported Google Calendar events (title, date and time, notes) is stored
**in SQLite on your device**. It is not sent to the Service's backend servers (v1.0.2
and later). Only the "completion state" of an event (a flag indicating whether it
was completed) is sent to the backend servers, for the purpose of tracking your
progress.

### Sharing with third parties
We do not sell, share, or transfer Google Calendar user data obtained through the
Service to any third party, including for advertising or analytics purposes.

### Compliance with the Google API Services User Data Policy
The Service's use of information received from Google APIs adheres to the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy)
(the "Policy"), including the
[Limited Use](https://developers.google.com/terms/api-services-user-data-policy#limited-use)
requirements. Specifically:

- Google Calendar data we obtain is used solely for the features disclosed to you
  in this Privacy Policy and in the app's user interface (timeline display and
  progress tracking).
- We never transfer or sell it to other users, use it for advertising, or use it as
  training data for machine learning models.
- No human reads Google user data beyond what is necessary to provide the features
  above, except where we have your explicit consent, where required by law, or
  where the data is aggregated and anonymised for internal operations.

### How to delete the data
You can delete all Google Calendar data imported into the Service in either of the
following ways:

1. Select "Disconnect Google Calendar" from the menu on the calendar screen.
2. Delete your account (Settings → Delete account) — all data is deleted both from
   your device and from our servers.

### Further information
See Google's privacy policy at
[https://policies.google.com/privacy](https://policies.google.com/privacy).

---

## Article 10 (Email delivery: Resend)

We use "Resend", an email delivery service provided by Resend Inc., to reply to
enquiries and to send important announcements.

### Information sent to Resend
- The recipient's email address (obtained from an OAuth provider, or entered by you
  when making an enquiry)
- The body and subject of the email

### Purposes
- Individual replies to enquiries
- Account-related notifications (where necessary)

### Further information
See Resend's privacy policy at
[https://resend.com/legal/privacy-policy](https://resend.com/legal/privacy-policy).

---

## Article 11 (Payment processing: Apple App Store and RevenueCat)

Since v1.0.1 (July 2026) the Service offers in-app purchases (one-time Diamond
packs). We use the following external services for payment processing and receipt
validation.

### 11-1. Apple App Store (payment processing)

Payments for in-app purchases are processed through the "App Store" operated by
Apple Inc.

#### Information sent to Apple
- Your Apple ID (used directly by Apple at the time of payment; the Service itself
  does not obtain your Apple ID)
- Payment method information (the Service does not obtain any of this)

#### Further information
See Apple's privacy policy at
[https://www.apple.com/legal/privacy/](https://www.apple.com/legal/privacy/).

### 11-2. RevenueCat (receipt validation and purchase history management)

We use "RevenueCat", provided by RevenueCat, Inc., to validate purchase receipts and
manage purchase history.

#### Information sent to RevenueCat
- An internal identifier of the Service (a value derived from the PlayerProfile ID)
- Purchase receipts obtained from the Apple App Store (records of one-time purchases)
- The purchased product ID, purchase time, and price information
- Device information (OS, app version, country/region)

#### Information not sent to RevenueCat
- Your email address
- Your name or nickname
- Confidential information such as authentication tokens or passwords

#### Where the data is stored
RevenueCat's cloud infrastructure (US region).

#### Purposes
- Validating purchase receipts (preventing fraudulent purchases)
- Managing purchase history
- Statistical analysis relating to purchases (aggregate figures such as ARPU and
  purchase completion rate)

#### Deletion
When you delete your account, we send a deletion request for the identifier
associated with your use of the Service on RevenueCat. Purchase history retained by
the Apple App Store is under Apple Inc.'s control and cannot be deleted by us.

#### Further information
See RevenueCat's privacy policy at
[https://www.revenuecat.com/privacy](https://www.revenuecat.com/privacy).

---

## Article 12 (Where data is stored: Render)

The Service's backend servers and database run on the cloud infrastructure of
"Render", provided by Render Services Inc.

### Data stored
- User account information (email address, display name, authentication identifiers)
- All data created within the Service (habits, timeline entries, characters, gacha
  history, etc.)
- Event data imported from Google Calendar

### Storage region
Singapore (Asia Pacific).

### Security
Communications are encrypted with TLS, and the database is accessible only from
authenticated backend servers.

### Further information
See Render's privacy policy at [https://render.com/privacy](https://render.com/privacy).

---

## Article 13 (Deletion of data)

You can delete your account and all associated data using "Settings → Delete
account" in the Service.

### Data that is deleted
- All data on the Service's backend servers, including your user account, habits,
  timeline entries, characters, and gacha history
- Authentication records in Firebase Authentication
- Behavioural analytics data in PostHog

### Data that is not deleted (statistics only)
- Feedback provided at the time of account deletion (where you choose to enter it)
  is retained in a form that cannot identify you, for statistical purposes aimed at
  improving the Service.

### Data that is not deleted (external services)
- The history of emails exchanged with you when handling enquiries remains with
  Resend.
- If you used a version released before v1.0 (29 May 2026) and events were written
  from the Service to your Google Calendar during that period, those events remain
  in Google Calendar. Please delete them yourself from Google Calendar. (The export
  feature was discontinued in v1.0, so no new data is written to Google Calendar.)
- If you have made in-app purchases, the purchase history held by the Apple App
  Store is under Apple Inc.'s control and cannot be deleted by us. Please review it
  from the purchase history screen of your Apple ID.

### Restoration
Deleted data cannot be restored, so please consider carefully before proceeding.

---

## Article 14 (Revisions)

We may revise this Privacy Policy as necessary. If there is a significant change, we
will notify you within the Service.

You can review the history of past revisions in the commit history of the GitHub
repository where this document is published.

---

## Appendix A — Your California privacy rights

This section applies if you are a resident of California. It supplements, and does
not replace, the rest of this Privacy Policy.

### Categories of personal information we collect

Over the past 12 months we have collected the categories of personal information
described in Article 2, namely: identifiers (name or nickname, email address,
provider UID, internal identifiers, device token), commercial information (records
of in-app purchases), internet or other electronic network activity information
(in-app events, screen transitions, crash and performance data), and the content you
create in the Service (habits, notes, timeline entries).

We collect this information for the purposes described in Article 3, from you
directly and from the OAuth provider you sign in with.

### We do not sell or share your personal information

We do not sell your personal information, and we do not share it for cross-context
behavioural advertising, as those terms are defined by California law. We have not
done so in the past 12 months. We do not knowingly collect or sell the personal
information of minors under 16.

### Your rights

Subject to the limits set by law, you have the right to:

- **Know** what personal information we have collected about you, and how we use and
  disclose it
- **Delete** the personal information we hold about you
- **Correct** inaccurate personal information
- **Opt out** of the sale or sharing of personal information (as noted above, we do
  not do either)
- **Not be discriminated against** for exercising any of these rights

### How to exercise them

The fastest route is "Settings → Delete account" in the app, which deletes your
account and the associated data described in Article 13. For any other request, or
if you would like us to act on your behalf, contact us using "Settings → Contact" in
the app. We will verify your request through the email address associated with your
account before acting on it.

---

## Contact

For enquiries about this Privacy Policy, please contact us from "Settings → Contact"
in the Service's app.

---

<p style="color: #666; font-size: 0.9em; text-align: center; margin-top: 40px;">
  © 2026 Sabiowl. All rights reserved.<br>
  <a href="{{ '/' | relative_url }}">← Back to top</a>
</p>
