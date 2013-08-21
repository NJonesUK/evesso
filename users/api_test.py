import evelink

api = evelink.api.API(api_key=(1781152, '5ik9w9O7aXXqglxyg8Gj4wpCHWKFSIRdzikX0PRXdLgK0BTQiQk020LUlRLLNLrW'))
account = evelink.account.Account(api=api)
key_info = account.key_info()

REQUIRED_API_ACCESS = (33554432,  # Account Status
                        16777216,  # Private CharacterInfo
                        8388608,  # Public CharacterInfo
                        64,  # FacWarStats
                        #8,  # CharacterSheet
                        )

ACCESS_MASK = sum(REQUIRED_API_ACCESS)


result = ACCESS_MASK - (ACCESS_MASK & key_info['access_mask'])
if result > 0:
    print "Key not valid"
else:
    print "Key valid"

# care about:
# AccountStatus
# CharacterInfo (both)
# FacWarStats
# CharacterSheet