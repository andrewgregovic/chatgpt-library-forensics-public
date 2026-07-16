# Representation-state model

The central descriptive finding is not that files “exist” or “do not exist.” It is that several observable states can diverge:

    displayed filename
      -> Library row
      -> explicit picker eligibility
      -> semantic search result
      -> parsed representation
      -> attached object
      -> current retrievable bytes
      -> runtime-local materialisation

This arrow chain is not a guaranteed pipeline. Each state is a different observation boundary. A positive observation at one boundary does not safely prove a positive observation at the next, and a failure at one does not prove absence at all others.

Examples in the submitted record include a Library-visible item that is not downstream reusable, a search/reference result that does not resolve an independently usable object, and current local bytes whose historical product route is not independently established.

The model is deliberately non-mechanistic. It does not identify an internal datastore, indexer, picker service, authorization grant, or monitoring system.
