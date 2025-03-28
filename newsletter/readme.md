## Introduction

This report outlines the results of a test conducted to determine the effectiveness of rewriting a specific block of a newsletter to avoid Gmail clipping. The goal is to reduce the email size while maintaining content quality and accessibility.

## Gmail Clipping

Gmail clips emails that exceed 102 KB in size. This results in a message at the bottom of the email indicating that the content has been truncated, which could negatively impact the user experience. Our goal is to ensure the email stays under this limit to prevent clipping.

## Tests

Every file size is measured in bytes and represents the actual file size, not the size on disk.  
To save time and allow for more iterations, we extracted a block from the largest available newsletter, redesigned and redeveloped it to see if we could improve its file size.

File size command: `stat -f "%z" [filename] | awk '{print $1 / 1024 " KB"}'`

| File Size  | File      | Description        | Reduction |
| ---------- | --------- | ------------------ | --------- |
| 18.5977 KB | base.html | Original block     | 0%        |
| 7.21289 KB | new.html  | New Stratsha block | 38.7837%  |
| 2.03809 KB | text.txt  | Only text          | 10.9588%  |

### Analysis

The tests are based on a single section. Let's analyze whether the results seem correct.

The "old block" comes from the largest newsletter provided by the client, which is Newsletter 12, segment 5042.

The full newsletter file size is `373.145 KB`, and it contains 21 sections (including the footer), meaning each section would be approximately `17.7688 KB` in size.  
Since our block size is less than `1 KB` away from this estimate, we can assume that the following calculations are reasonably accurate.

Using the old block, the estimated newsletter size would be `390.5517 KB`.  
Using the new block, the estimated newsletter size would be `151.47069 KB`.

## Key Takeaways

- The new block reduces the size by 38.78%, making it significantly smaller than the original block.
- Despite the reduction, the email size still exceeds Gmail’s clipping limit by 33%, meaning further adjustments are necessary.
- To avoid clipping, we may need to simplify the design, reduce text, or cut some accessibility features.
