"""Birth data — when and where the native was born."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class BirthData:
    name: str
    # Local civil date & time of birth, *naive* — interpret in `tz_id`.
    local_birth_moment: datetime
    tz_id: str                # IANA timezone, e.g. "America/New_York"
    latitude: float           # degrees, positive north
    longitude: float          # degrees, positive east
    place_name: str

    @property
    def utc_instant(self) -> datetime:
        """Convert the local civil moment to a tz-aware UTC datetime."""
        try:
            from zoneinfo import ZoneInfo
        except ImportError:  # pragma: no cover — Python < 3.9
            from backports.zoneinfo import ZoneInfo  # type: ignore
        local = self.local_birth_moment
        if local.tzinfo is None:
            local = local.replace(tzinfo=ZoneInfo(self.tz_id))
        return local.astimezone(timezone.utc)

    @property
    def julian_day_ut(self) -> float:
        """Julian Day (UT) for Swiss Ephemeris."""
        utc = self.utc_instant
        # 2440587.5 corresponds to 1970-01-01 00:00 UTC (the Unix epoch).
        return 2440587.5 + utc.timestamp() / 86400.0
