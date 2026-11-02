#!/bin/bash
# A7 vendor-provenance crawl: fetch contractor-cohort vendor pages via curl, save raw
# HTML/text under research/provenance/ for candidate extraction. Read-only fetches,
# polite delays, fixed target list from /tmp/provenance_targets.txt.
cd "/Users/faisal.muthalib/Documents/VibeProject/O&G_Technologies_Library/hilir-tech-library" || exit 1
mkdir -p research/provenance
while read -r id url; do
  [ -z "$id" ] && continue
  for path in "" "/about" "/resources" "/news" "/standards" "/technology" "/certifications"; do
    f="research/provenance/${id}$(echo "$path" | tr '/' '_').txt"
    [ -s "$f" ] && continue
    curl -sL --max-time 20 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)" "${url}${path}" -o "$f" 2>/dev/null
    sleep 2
  done
  echo "crawled $id"
done < /tmp/provenance_targets.txt
echo "A7 crawl finished $(date)"
